from fastapi import APIRouter

from src.app.channel import service

from .model import AddChannelReq

router = APIRouter(prefix="/channel", tags=["channel"])


@router.get("/")
async def get_channel():
  result = await service.getChannelList()
  return result


@router.post("/")
async def add_channel(body: AddChannelReq):
  await service.addChannel(body)
  return 0
