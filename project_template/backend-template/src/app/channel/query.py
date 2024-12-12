from sqlmodel import select

from src.api.channel.model import Channel
from src.config import db


def addChannel(channel: Channel):
  session = db.getCurrentSession()
  session.add(channel)


async def selectAllChannel():
  statement = select(Channel)

  session = db.getCurrentSession()
  results = await session.exec(statement)
  return results
