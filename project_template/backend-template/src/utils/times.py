import datetime
import time


def printTime():
  start = time.time()

  return lambda: print(f"Execute: {time.time() - start:.5f} sec")


# https://spoqa.github.io/2019/02/15/python-timezone.html
def utcnow():
  return datetime.datetime.now(datetime.UTC)
