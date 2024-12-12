import abc

from starlette.types import ASGIApp, Receive, Scope, Send


# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-middleware
# https://www.starlette.io/middleware/
class FastAPIMiddleware(metaclass=abc.ABCMeta):
  def __init__(self, app: ASGIApp) -> None:
    self.app = app

  @abc.abstractmethod
  async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
    pass
