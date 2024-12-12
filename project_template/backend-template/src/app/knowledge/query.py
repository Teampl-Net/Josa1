from typing import List

from sqlalchemy import text

from src.config import db


async def getKnowList(collection_id: str) -> List[str]:
  session = db.getCurrentSession()

  connection = await session.connection()

  query = text(
    f"SELECT document FROM public.langchain_pg_embedding where collection_id = '{collection_id}'"
  )
  result = await connection.execute(query)
  doc_list = [row.document for row in result]
  doc_list.reverse()
  return doc_list
