# first stage
FROM python:3.11.5-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
 	&& pip install --no-cache-dir --user -r requirements.txt \
	&& rm -rf /var/lib/apt/lists/*


# final stage
FROM python:3.11.5-slim

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local

# update PATH environment variable
ENV PATH=/root/.local/bin:$PATH

WORKDIR /code

COPY ./duckduckgo_search_api /code/duckduckgo_search_api

CMD ["uvicorn", "duckduckgo_search_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "warning"]
