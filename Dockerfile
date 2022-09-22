# first stage
FROM python:3-alpine AS builder

# install orjson
# RUN apk add --no-cache gcc g++ musl-dev rust cargo patchelf
# pip install -U orjson

COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --no-cache-dir --upgrade --user -r requirements.txt

# second unnamed stage
FROM python:3-alpine

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local

# update PATH environment variable
ENV PATH=/root/.local/bin:$PATH

WORKDIR /code

COPY ./duckduckgo_search_api /code/duckduckgo_search_api

CMD ["uvicorn", "duckduckgo_search_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "warning"]
