import asyncio
import functools
import os
import sys
from contextvars import ContextVar
from typing import Awaitable, Callable, Optional, TypeVar

import sqlalchemy.ext.asyncio as sqlalchemyAsyncIo
import starlette.status as HTTPStatus
from dotenv import load_dotenv
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from src.libs.aa_pgvector import Aa_PGVector

from . import ai, logging

load_dotenv()

CONNECTION_STRING = Aa_PGVector.connection_string_from_db_params(
  driver=os.environ.get("PGVECTOR_DRIVER", "psycopg"),
  host=os.environ.get("PGVECTOR_HOST", "172.24.43.169"),
  port=int(os.environ.get("PGVECTOR_PORT", "5432")),
  database=os.environ.get("PGVECTOR_DATABASE", "postgres"),
  user=os.environ.get("PGVECTOR_USER", "postgres"),
  password=os.environ.get("PGVECTOR_PASSWORD", "susoft1!"),
)
print(CONNECTION_STRING)

# https://dev.to/uponthesky/python-post-reviewhow-to-implement-a-transactional-decorator-in-fastapi-sqlalchemy-ein
# https://cloud.google.com/appengine/docs/legacy/standard/python/datastore/transactions?hl=ko
# https://github.com/teamhide/fastapi-boilerplate/blob/master/core/db/session.py
# https://hides.kr/1103
## Session #####################################################################
# some hints from: https://github.com/teamhide/fastapi-boilerplate/blob/master/core/db/session.py
db_session_context: ContextVar[Optional[int]] = ContextVar("db_session_context", default=None)
engine = sqlalchemyAsyncIo.create_async_engine(url=CONNECTION_STRING, echo=True)
sync_engine = engine.sync_engine

if sys.platform == "win32":
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def getDbSessionContext() -> int:
  session_id = db_session_context.get()

  if not session_id:
    raise ValueError("Currently no session is available")

  return session_id


def setDbSessionContext(*, session_id: Optional[int]) -> None:
  db_session_context.set(session_id)


asyncScopedSession = sqlalchemyAsyncIo.async_scoped_session(
  session_factory=sqlalchemyAsyncIo.async_sessionmaker(
    bind=engine, autoflush=False, autocommit=False, class_=AsyncSession
  ),
  scopefunc=getDbSessionContext,
)


def getCurrentSession() -> AsyncSession:
  return asyncScopedSession()


def getCurrentSyncSession():
  return getCurrentSession().sync_session


## Init ########################################################################
def createdDbAndTables():
  SQLModel.metadata.create_all(sync_engine)


## Vector engine ###############################################################
def getDbByCollection(collection_name: str):
  db = Aa_PGVector(
    connection=CONNECTION_STRING,
    # connection=sync_engine,
    # session_maker=getCurrentSyncSession,
    collection_name=collection_name,
    embeddings=ai.embeddings,
  )
  return db


def getRetrieverByCollection(collection_name: str):
  db = getDbByCollection(collection_name)
  return db.as_retriever(
    search_type="similarity_score_threshold", search_kwargs={"k": 5, "score_threshold": 0.4}
  )


## Transaction #################################################################
T = TypeVar("T")
AsyncCallable = Callable[..., Awaitable[T]]
logger = logging.getLogger(__file__)


def transactional(func: AsyncCallable[T]) -> AsyncCallable[T]:
  @functools.wraps(func)
  async def _wrapper(*args, **kwargs) -> T:
    try:
      db_session = getCurrentSession()

      if db_session.in_transaction():
        return await func(*args, **kwargs)

      async with db_session.begin():
        # automatically committed / rolled back thanks to the context manager
        return_value = await func(*args, **kwargs)

      return return_value
    except Exception as error:
      logger.info(f"request hash: {getDbSessionContext()}")
      logger.exception(error)
      raise

  return _wrapper


## MiddleWare ##################################################################
class DBSessionMiddleware(BaseHTTPMiddleware):
  async def dispatch(
    self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
  ) -> Response:
    response = Response(
      "Internal server error", status_code=HTTPStatus.HTTP_500_INTERNAL_SERVER_ERROR
    )

    try:
      setDbSessionContext(session_id=hash(request))
      response = await call_next(request)
    finally:
      await asyncScopedSession.remove()  # this includes closing the session as well
      setDbSessionContext(session_id=None)
    return response
