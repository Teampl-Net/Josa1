from typing import List

from pydantic import BaseModel


class AddKnowledgeReq(BaseModel):
  knowledge: List[str]


class SearchKnowledgeReq(BaseModel):
  question: str
