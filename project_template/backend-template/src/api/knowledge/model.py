from typing import List

from pydantic import BaseModel


class AddKnowListReq(BaseModel):
  knowList: List[str]
  collection_id: str
