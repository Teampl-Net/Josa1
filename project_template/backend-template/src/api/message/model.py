from pydantic import BaseModel


class MessageReq(BaseModel):
  question: str
  collection_id: str
