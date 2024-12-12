from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from src.app.message import service

from .model import MessageReq

router = APIRouter(prefix="/message", tags=["message"])


@router.post("/")
async def search_knowledge(body: MessageReq):
  return StreamingResponse(service.createStream(body), media_type="text/event-stream")
