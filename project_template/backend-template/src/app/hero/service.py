from typing import List

from src.api.hero.model import Hero
from src.config.db import transactional

from . import query


@transactional
async def addHero(hero: Hero):
  query.addHero(hero)
  return hero


@transactional
async def addHeroWithError(hero: Hero):
  query.addHero(hero)
  raise Exception("Error!!")
  return hero


@transactional
async def addDoubleHero(hero1: Hero, hero2: Hero):
  first_hero = await addHero(hero1)
  second_hero = await addHeroWithError(hero2)
  return [first_hero, second_hero]


@transactional
async def addHeroList(hero_list: List[Hero]):
  query.addHeroList(hero_list)
  return hero_list


@transactional
async def selectAllHero():
  results = await query.selectAllHero()
  for hero in results:
    print(hero)
  return results.all()


@transactional
async def selectHeroByName(name: str):
  print("")
