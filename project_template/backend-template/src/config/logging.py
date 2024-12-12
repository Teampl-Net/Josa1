import logging

from src.utils import times

from .fastapi import FastAPIMiddleware

# https://docs.python.org/ko/3/howto/logging.html
# create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
  fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y/%m/%d %I:%M:%S %p"
)
console_handler.setFormatter(formatter)


def getLogger(name: str | None = None):
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)

  return logger


# logger.debug("This message should go to the log file")
# logger.info("So should this")
# logger.warning("And this, too")
# logger.error("And non-ASCII stuff, too, like Øresund and Malmö")


## Middleware ##################################################################
class ExecuteTimeLogMiddleware(FastAPIMiddleware):
  async def __call__(self, scope, receive, send):
    end = times.printTime()
    await self.app(scope, receive, send)
    end()
