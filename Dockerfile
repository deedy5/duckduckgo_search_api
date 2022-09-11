FROM python:3-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./duckduckgo_search_api /code/duckduckgo_search_api
CMD ["uvicorn", "duckduckgo_search_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "critical"]
