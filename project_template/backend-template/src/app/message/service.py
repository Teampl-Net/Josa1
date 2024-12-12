import orjson
from langchain_core.prompts import PromptTemplate

from src.api.message.model import MessageReq
from src.config.ai import llm
from src.config.db import getRetrieverByCollection

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


async def createStream(search_req: MessageReq):
  print("요청", search_req)

  req_msg = search_req.question

  retriever = getRetrieverByCollection(search_req.collection_id)
  knowledges = await retriever.aget_relevant_documents(req_msg)
  print(knowledges)
  if len(knowledges) > 0:
    knowledge_contents = "".join(
      [f"{document.page_content}" for i, document in enumerate(knowledges)]
    )
    print(knowledge_contents)
    yield (
      '{"knowledge": '
      + orjson.dumps([document.page_content for document in knowledges]).decode()
      + ', "body": "'
    )

    async for chunk in search_chain.astream({"question": req_msg, "knowledge": knowledge_contents}):
      print(chunk.content, end="", flush=True)
      if isinstance(chunk.content, str):
        yield chunk.content
      else:
        yield str(chunk.content)
    yield '"}'
  else:
    yield '{"knowledge": [], "body": "지식을 찾지 못했습니다."}'
