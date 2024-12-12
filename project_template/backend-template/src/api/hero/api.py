from typing import List, Sequence

from fastapi import APIRouter

from src.app.hero import service

from .model import AddHeroResponse, DoubleHero, Hero

router = APIRouter(prefix="/hero", tags=["hero"])


@router.post("/", response_model=AddHeroResponse)
async def addHero(body: Hero):
  hero = await service.addHero(body)
  if hero.id is None:
    raise ValueError("Hero ID is None")
  return AddHeroResponse(id=hero.id)


@router.post("/transaction", response_model=List[int])
async def addHeroWithError(body: DoubleHero):
  hero_list = await service.addDoubleHero(body.hero1, body.hero2)
  hero_id_list = [hero.id for hero in hero_list]
  return hero_id_list


@router.post("/bulk", response_model=List[int])
async def addHeroList(body: List[Hero]):
  hero_list = await service.addHeroList(body)
  hero_id_list = [hero.id for hero in hero_list]
  return hero_id_list


@router.get("/bulk", response_model=Sequence[Hero])
async def selectAllHero():
  hero_list = await service.selectAllHero()
  return hero_list
