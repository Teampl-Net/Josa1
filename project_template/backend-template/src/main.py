from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

# from sqlmodel import Field, SQLModel
# from src.api.hero import api as hero
from src.api.channel import api as channel
from src.api.knowledge import api as knowledge
from src.api.message import api as message
from src.config.db import DBSessionMiddleware
from src.config.logging import ExecuteTimeLogMiddleware

# class Hero(SQLModel, table=True):
#   id: Optional[int] = Field(default=None, primary_key=True)
#   name: str
#   secret_name: str
#   age: Optional[int] = None


# from src.routes import search

load_dotenv()

# # https://fastapi.tiangolo.com/advanced/events/#startup-event
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#   # on startup
#   createdDbAndTables()
#   yield
#   # on shutdown

app = FastAPI(
  title="Mankik LLM Server",
  version="1.0",
  description="A simple API server using OpenAI",
  default_response_class=ORJSONResponse,
  # lifespan=lifespan,
)

# If You need CORS
# @see https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(ExecuteTimeLogMiddleware)
app.add_middleware(DBSessionMiddleware)
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=False,
  allow_methods=["*"],
  allow_headers=["*"],
)

# app.include_router(hero.router)
app.include_router(channel.router)
app.include_router(knowledge.router)
app.include_router(message.router)


# app.include_router(search.router)
@app.get("/test")
async def root():
  return {"message": "Hello World"}


# @app.post("/hero")
# @transactional
# async def add_hero():
#   hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
#   hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
#   hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

#   session = getCurrentSession()
#   session.add_all([hero_1, hero_2, hero_3])


# @app.post("/hero_error")
# @transactional
# async def add_hero_error():
#   hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
#   hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
#   hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

#   session = getCurrentSession()
#   session.add_all([hero_1, hero_2, hero_3])
#   raise Exception("Error")


if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="localhost", port=18081)
