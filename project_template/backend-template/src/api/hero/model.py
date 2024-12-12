from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str = Field(index=True)
  secret_name: str
  age: Optional[int] = Field(default=None, index=True)

  team_id: int | None = Field(default=None, foreign_key="team.id")


class DoubleHero(BaseModel):
  hero1: Hero
  hero2: Hero


class AddHeroResponse(BaseModel):
  id: int
