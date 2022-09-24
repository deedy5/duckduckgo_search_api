# temp stage
FROM python:3-alpine AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install orjson
# RUN apk add --no-cache gcc g++ musl-dev rust cargo patchelf
# pip install -U orjson

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


# finald stage
FROM python:3-alpine

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY ./duckduckgo_search_api /app/duckduckgo_search_api

CMD ["uvicorn", "duckduckgo_search_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "warning"]
