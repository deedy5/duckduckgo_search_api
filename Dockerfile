# first stage
FROM python:3-alpine AS builder

# install orjson
# RUN apk add --no-cache gcc g++ musl-dev rust cargo patchelf
# pip install -U orjson

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps alpine-sdk musl-dev \
 && pip install --upgrade --no-cache-dir pip setuptools \
 && pip install --upgrade --no-cache-dir cython \
 && pip install --upgrade --no-cache-dir --user -r requirements.txt \
 && apk --purge del .build-deps


# final stage
FROM python:3-alpine

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local

# update PATH environment variable
ENV PATH=/root/.local/bin:$PATH

WORKDIR /code

COPY ./duckduckgo_search_api /code/duckduckgo_search_api

CMD ["uvicorn", "duckduckgo_search_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "warning"]
