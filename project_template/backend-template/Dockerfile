### Infos ######################################################################
## Base Images:
# https://hub.docker.com/_/python

### Base #######################################################################
FROM python:3.11-alpine as base

WORKDIR /app

### Builder ####################################################################
FROM base as builder

RUN pip install poetry==1.8.2

# https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR \
    poetry install --without dev

### Runtime ####################################################################
FROM base as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    BIND="unix:/tmp/gunicorn.sock" \
    FASTAPI_ENV=production

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY ./gunicorn_conf.py ./gunicorn_conf.py

EXPOSE 18081

ENTRYPOINT ["gunicorn"]

### Production #################################################################
FROM runtime as prod

# Local 위치, Image 내부 위치
COPY ./src ./src

CMD [ \
    "-c", "./gunicorn_conf.py", \
    "src.main:app" \
    ]

### Development ################################################################
FROM runtime as dev

ENV WORKER_CLASS="src.utils.worker.RestartableUvicornWorker" \
    WEB_CONCURRENCY="1"

CMD [ \
    "--reload", \
    "-c", "./gunicorn_conf.py", \
    "src.main:app" \
    ]
