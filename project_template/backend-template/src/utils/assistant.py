from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from openai import OpenAI

from src.settings import EMBEDDING_MODEL

load_dotenv()

client = OpenAI()
# llm = ChatOpenAI(model="gpt-3.5-turbo")  # gpt-3.5-turbo
llm = ChatOpenAI(model="gpt-4-turbo")  # gpt-3.5-turbo
embeddings = OpenAIEmbeddings(
  # https://platform.openai.com/docs/models/embeddings
  model=EMBEDDING_MODEL
)
