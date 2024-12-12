from typing import List

import sqlmodel

from src.api.hero.model import Hero
from src.config import db


## Create ######################################################################
def addHero(hero: Hero):
  session = db.getCurrentSession()
  session.add(hero)


def addHeroList(hero_list: List[Hero]):
  session = db.getCurrentSession()
  session.add_all(hero_list)


## Read ########################################################################
async def selectAllHero():
  statement = sqlmodel.select(Hero)

  session = db.getCurrentSession()
  results = await session.exec(statement)
  return results


async def selectHeroById(id: int):
  session = db.getCurrentSession()
  result = await session.get(Hero, id)
  return result


async def selectHeroByName(name: str):
  statement = sqlmodel.select(Hero).where(Hero.name == name)

  session = db.getCurrentSession()
  results = await session.exec(statement)
  return results


async def selectHeroByAge(start: int, end: int):
  statement = sqlmodel.select(Hero).where(
    # And 조건, col은 Optional 타입일 때 사용
    sqlmodel.col(Hero.age) >= start,
    sqlmodel.col(Hero.age) <= end,
  )

  session = db.getCurrentSession()
  results = await session.exec(statement)
  return results


async def selectHeroByAnyName(name: str, secret_name: str):
  statement = (
    # or은 sqlmodel.or_을 이용, .limit() 또는 .offset()도 가능
    sqlmodel.select(Hero)
    .where(sqlmodel.or_(Hero.name == name, Hero.secret_name == secret_name))
    .limit(10)
  )

  session = db.getCurrentSession()
  results = await session.exec(statement)
  return results


## Update ######################################################################
async def updateHeroAgeByName(name: str, age: int):
  statement = sqlmodel.select(Hero).where(Hero.name == name)

  session = db.getCurrentSession()
  result = await session.exec(statement)
  hero_1 = result.one()

  hero_1.age = age
  session.add(hero_1)
  return hero_1


## Delete ######################################################################
async def deleteHeroAgeById(id: int):
  session = db.getCurrentSession()

  hero_1 = await session.get_one(Hero, id)

  await session.delete(hero_1)
  return hero_1
