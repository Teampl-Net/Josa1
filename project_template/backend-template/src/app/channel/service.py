from src.api.channel.model import AddChannelReq, Channel
from src.config.db import transactional

from . import query


@transactional
async def addChannel(add_req: AddChannelReq):
  new_channel = Channel(name=add_req.name, category="test")
  query.addChannel(new_channel)


async def getChannelList():
  result = await query.selectAllChannel()
  return result.all()
