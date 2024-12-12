from fastapi import APIRouter

from src.app.knowledge import service

from .model import AddKnowListReq

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


@router.get("/")
async def get_knowledge(collection_id: str):
  result = await service.getKnowList(collection_id)
  return result


@router.post("/")
async def add_knowledge(body: AddKnowListReq):
  await service.addKnowlegeList(body)
