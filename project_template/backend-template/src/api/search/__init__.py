from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from src.utils.times import print_time

from .model import AddKnowledgeReq, SearchKnowledgeReq
from .service import add_knowlege_list, create_stream

router = APIRouter(prefix="/search", tags=["search"])


@router.post("/add")
async def add_knowledge(body: AddKnowledgeReq):
  end_time = print_time()
  await add_knowlege_list(body)
  end_time()


@router.post("/knowledge")
async def search_knowledge(body: SearchKnowledgeReq):
  return StreamingResponse(create_stream(body), media_type="text/event-stream")
