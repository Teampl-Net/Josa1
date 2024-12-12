import logging
import uuid
from typing import Any, Callable, Iterable, List, Optional, Tuple, Union

import sqlalchemy
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import (
  _LANGCHAIN_DEFAULT_COLLECTION_NAME,
  DEFAULT_DISTANCE_STRATEGY,
  Base,
  DistanceStrategy,
)
from sqlalchemy.dialects.postgresql import JSON, JSONB, UUID, insert
from sqlalchemy.orm import Session, relationship, sessionmaker

from src.utils import times

_classes: Any = None


def _get_embedding_collection_store(vector_dimension: Optional[int] = None) -> Any:
  global _classes
  if _classes is not None:
    return _classes

  from pgvector.sqlalchemy import Vector  # type: ignore

  class CollectionStore(Base):
    """Collection store."""

    __tablename__ = "langchain_pg_collection"

    uuid = sqlalchemy.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    cmetadata = sqlalchemy.Column(JSON)

    embeddings = relationship("EmbeddingStore", back_populates="collection", passive_deletes=True)

    @classmethod
    def get_by_name(cls, session: Session, name: str) -> Optional["CollectionStore"]:
      return session.query(cls).filter(cls.name == name).first()  # type: ignore

    @classmethod
    def get_or_create(
      cls, session: Session, name: str, cmetadata: Optional[dict] = None
    ) -> Tuple["CollectionStore", bool]:
      """Get or create a collection.
      Returns:
           Where the bool is True if the collection was created.
      """  # noqa: E501
      created = False
      collection = cls.get_by_name(session, name)
      if collection:
        return collection, created

      collection = cls(name=name, cmetadata=cmetadata)
      session.add(collection)
      session.commit()
      created = True
      return collection, created

  class EmbeddingStore(Base):
    """Embedding store."""

    __tablename__ = "langchain_pg_embedding"

    id = sqlalchemy.Column(
      sqlalchemy.String, nullable=True, primary_key=True, index=True, unique=True
    )

    collection_id = sqlalchemy.Column(
      UUID(as_uuid=True),
      sqlalchemy.ForeignKey(f"{CollectionStore.__tablename__}.uuid", ondelete="CASCADE"),
    )
    collection = relationship(CollectionStore, back_populates="embeddings")

    embedding: Vector = sqlalchemy.Column(Vector(vector_dimension))  # type: ignore
    document = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cmetadata = sqlalchemy.Column(JSONB, nullable=True)

    ### CUSTOM DATA FIELD ##########################################################################
    sub_n1 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sub_n2 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    sub_n3 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    sub_s1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sub_s2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sub_s3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    sub_d1 = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), nullable=True)
    sub_d2 = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), nullable=True)
    sub_d3 = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), nullable=True)
    ################################################################################################

    __table_args__ = (
      sqlalchemy.Index(
        "ix_cmetadata_gin",
        "cmetadata",
        postgresql_using="gin",
        postgresql_ops={"cmetadata": "jsonb_path_ops"},
      ),
    )

  _classes = (EmbeddingStore, CollectionStore)

  return _classes


Connection = Union[sqlalchemy.engine.Engine, str]


class Aa_PGVector(PGVector):
  def __init__(
    self,
    embeddings: Embeddings,
    *,
    connection: Optional[Connection] = None,
    session_maker: Optional[Callable[[], Session]] = None,
    embedding_length: Optional[int] = None,
    collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
    collection_metadata: Optional[dict] = None,
    distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,
    pre_delete_collection: bool = False,
    logger: Optional[logging.Logger] = None,
    relevance_score_fn: Optional[Callable[[float], float]] = None,
    engine_args: Optional[dict[str, Any]] = None,
    use_jsonb: bool = True,
    create_extension: bool = True,
  ) -> None:
    """Initialize the PGVector store.

    Args:
        connection: Postgres connection string.
        embeddings: Any embedding function implementing
            `langchain.embeddings.base.Embeddings` interface.
        embedding_length: The length of the embedding vector. (default: None)
            NOTE: This is not mandatory. Defining it will prevent vectors of
            any other size to be added to the embeddings table but, without it,
            the embeddings can't be indexed.
        collection_name: The name of the collection to use. (default: langchain)
            NOTE: This is not the name of the table, but the name of the collection.
            The tables will be created when initializing the store (if not exists)
            So, make sure the user has the right permissions to create tables.
        distance_strategy: The distance strategy to use. (default: COSINE)
        pre_delete_collection: If True, will delete the collection if it exists.
            (default: False). Useful for testing.
        engine_args: SQLAlchemy's create engine arguments.
        use_jsonb: Use JSONB instead of JSON for metadata. (default: True)
            Strongly discouraged from using JSON as it's not as efficient
            for querying.
            It's provided here for backwards compatibility with older versions,
            and will be removed in the future.
        create_extension: If True, will create the vector extension if it
            doesn't exist. disabling creation is useful when using ReadOnly
            Databases.
    """
    self.embedding_function = embeddings
    self._embedding_length = embedding_length
    self.collection_name = collection_name
    self.collection_metadata = collection_metadata
    self._distance_strategy = distance_strategy
    self.pre_delete_collection = pre_delete_collection
    self.logger = logger or logging.getLogger(__name__)
    self.override_relevance_score_fn = relevance_score_fn

    if isinstance(connection, str):
      self._engine = sqlalchemy.create_engine(url=connection, **(engine_args or {}))
    elif isinstance(connection, sqlalchemy.engine.Engine):
      self._engine = connection
    else:
      raise ValueError(
        "connection should be a connection string or an instance of " "sqlalchemy.engine.Engine"
      )

    if session_maker:
      self._session_maker = session_maker
    else:
      self._session_maker = sessionmaker(bind=self._engine)

    self.use_jsonb = use_jsonb
    self.create_extension = create_extension

    if not use_jsonb:
      # Replace with a deprecation warning.
      raise NotImplementedError("use_jsonb=False is no longer supported.")
    self.__post_init__()

  def __post_init__(self) -> None:
    """Initialize the store."""
    if self.create_extension:
      self.create_vector_extension()

    EmbeddingStore, CollectionStore = _get_embedding_collection_store(self._embedding_length)
    self.CollectionStore = CollectionStore
    self.EmbeddingStore = EmbeddingStore
    self.create_tables_if_not_exists()
    self.create_collection()

  def add_embeddings(
    self,
    texts: Iterable[str],
    embeddings: List[List[float]],
    metadatas: Optional[List[dict]] = None,
    ids: Optional[List[str]] = None,
    lc_kwargs: Optional[List[dict[str, Any]]] = None,
    **kwargs: Any,
  ) -> List[str]:
    """Add embeddings to the vectorstore.

    Args:
        texts: Iterable of strings to add to the vectorstore.
        embeddings: List of list of embedding vectors.
        metadatas: List of metadatas associated with the texts.
        kwargs: vectorstore specific parameters
    """
    if ids is None:
      ids = [str(uuid.uuid4()) for _ in texts]

    if not metadatas:
      metadatas = [{} for _ in texts]

    if not lc_kwargs:
      lc_kwargs = [{} for _ in texts]

    with self._session_maker() as session:  # type: ignore[arg-type]
      collection = self.get_collection(session)
      if not collection:
        raise ValueError("Collection not found")
      data = [
        {
          "id": id,
          "collection_id": collection.uuid,
          "embedding": embedding,
          "document": text,
          "cmetadata": metadata or {},
          ### CUSTOM DATA FIELD ####################################################################
          "sub_n1": lc_kwarg["sub_n1"] or 0,
          "sub_n2": lc_kwarg["sub_n3"] or 0,
          "sub_n3": lc_kwarg["sub_n3"] or 0,
          "sub_s1": lc_kwarg["sub_s1"] or "",
          "sub_s2": lc_kwarg["sub_s2"] or "",
          "sub_s3": lc_kwarg["sub_s3"] or "",
          "sub_d1": lc_kwarg["sub_d1"] or times.utcnow(),
          "sub_d2": lc_kwarg["sub_d2"] or times.utcnow(),
          "sub_d3": lc_kwarg["sub_d3"] or times.utcnow(),
          ###########################################################################3##############
        }
        for text, metadata, embedding, id, lc_kwarg in zip(
          texts, metadatas, embeddings, ids, lc_kwargs
        )
      ]
      stmt = insert(self.EmbeddingStore).values(data)
      on_conflict_stmt = stmt.on_conflict_do_update(
        index_elements=["id"],
        # Conflict detection based on these columns
        set_={
          "embedding": stmt.excluded.embedding,
          "document": stmt.excluded.document,
          "cmetadata": stmt.excluded.cmetadata,
        },
      )
      session.execute(on_conflict_stmt)
      session.commit()

    return ids

  async def aadd_documents(self, documents: List[Document], **kwargs: Any) -> List[str]:
    """Run more documents through the embeddings and add to the vectorstore.

    Args:
        documents (List[Document]: Documents to add to the vectorstore.

    Returns:
        List[str]: List of IDs of the added texts.
    """
    texts = [doc.page_content for doc in documents]
    metadatas = [doc.metadata for doc in documents]
    lc_kwargs = [doc._lc_kwargs for doc in documents]
    return await self.aadd_texts(texts, metadatas, lc_kwargs=lc_kwargs)
