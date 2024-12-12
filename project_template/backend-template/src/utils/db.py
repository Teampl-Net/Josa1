import os

from langchain_postgres import PGVector

from .assistant import embeddings

COLLECTION_NAME = "SAEUM_SOFT"
CONNECTION_STRING = PGVector.connection_string_from_db_params(
  driver=os.environ.get("PGVECTOR_DRIVER", "psycopg"),
  host=os.environ.get("PGVECTOR_HOST", "localhost"),
  port=int(os.environ.get("PGVECTOR_PORT", "5432")),
  database=os.environ.get("PGVECTOR_DATABASE", "postgres"),
  user=os.environ.get("PGVECTOR_USER", "postgres"),
  password=os.environ.get("PGVECTOR_PASSWORD", "postgres"),
)

db = PGVector(
  connection=CONNECTION_STRING,
  collection_name=COLLECTION_NAME,
  embeddings=embeddings,
  use_jsonb=True,
)

retriever = db.as_retriever(
  search_type="similarity_score_threshold", search_kwargs={"k": 5, "score_threshold": 0.4}
)
