from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Channel(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str = Field(index=True)
  category: str = Field(default="")
  # cre_date: datetime = Field(default_factory=times.utcnow)
  collection_id: Optional[UUID] = Field(default=None, nullable=True)


class AddChannelReq(BaseModel):
  name: str = Field()
