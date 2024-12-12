from langchain_core.documents import Document

from src.api.knowledge.model import AddKnowListReq
from src.config.db import getRetrieverByCollection
from src.utils import times

from . import query


async def addKnowlegeList(add_req: AddKnowListReq):
  know_list = add_req.knowList

  retriever = getRetrieverByCollection(add_req.collection_id)
  if len(know_list) > 0:
    await retriever.aadd_documents(
      [
        Document(
          page_content=content,
          metadata={"source": "USER_INPUT"},
          # 커스텀 데이터
          sub_n1=0,
          sub_n2=1,
          sub_n3=2,
          sub_s1="",
          sub_s2="",
          sub_s3="",
          sub_d1=times.utcnow(),
          sub_d2=times.utcnow(),
          sub_d3=times.utcnow(),
        )
        for content in know_list
      ]
    )


async def getKnowList(collection_id: str):
  return await query.getKnowList(collection_id)
