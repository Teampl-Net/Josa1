from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from openai import OpenAI

### OpenAI ####################################################################
# -- Constants -----------------------------------------------------------------
# https://platform.openai.com/docs/models/
# Response JSON type requires: gpt-3.5-turbo-1106 | gpt-4-1106-preview
# The Retrieval tool requires: gpt-3.5-turbo-1106 | gpt-4-1106-preview
OPENAI_CHAT_MODEL = "gpt-4-turbo-preview"

# https://platform.openai.com/docs/models/embeddings
OPENAI_EMBEDDING_MODEL = "text-embedding-3-large"

# -- Runtime -------------------------------------------------------------------
load_dotenv()

client = OpenAI()
llm = ChatOpenAI(model=OPENAI_CHAT_MODEL)
embeddings = OpenAIEmbeddings(
  # https://platform.openai.com/docs/models/embeddings
  model=OPENAI_EMBEDDING_MODEL
)
