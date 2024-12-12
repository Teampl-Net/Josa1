from typing import List

from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate

from src.utils.assistant import llm
from src.utils.db import retriever

from .model import AddKnowledgeReq, SearchKnowledgeReq


async def add_knowlege_list(add_req: AddKnowledgeReq):
  knowledge = add_req.knowledge
  if len(knowledge) > 0:
    await retriever.aadd_documents(
      [Document(page_content=content, metadata={"source": "USER_INPUT"}) for content in knowledge]
    )


search_prompt = PromptTemplate.from_template(
  """지식을 활용하여 질문에 대한 답변하세요.
  단, 한문장으로 간결하게 답하세요.
  
  질문: {question}
  지식:
  {knowledge}
  답변:
  """
)
search_chain = search_prompt | llm


async def create_stream(search_req: SearchKnowledgeReq):
  print("요청", search_req)

  req_msg = search_req.question

  knowledges = await retriever.aget_relevant_documents(req_msg)
  print(knowledges)
  if len(knowledges) > 0:
    knowledge_contents = numbered_knowledge(knowledges)
    print(knowledge_contents)
    yield f"찾은 지식:\n{knowledge_contents}\n\n"

    async for chunk in search_chain.astream({"question": req_msg, "knowledge": knowledge_contents}):
      print(chunk.content, end="", flush=True)
      yield chunk.content
  else:
    async for chunk in llm.astream(req_msg):
      print(chunk.content, end="", flush=True)
      yield chunk.content


def numbered_knowledge(knowledge: List[Document]) -> str:
  return "\n".join([f"{i+1}. {document.page_content}" for i, document in enumerate(knowledge)])
