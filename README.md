#  duckduckgo_search_api

Fastapi code to deploy an API that pulls data from duckduckgo search engine.
___
## 1) Usage
**clone**
```python3
git clone https://github.com/deedy5/duckduckgo_search_api.git
cd duckduckgo_search_api
```
**run**
```python3
python -m pip install -U -r requirements.txt
python start.py
```

**check**</br>
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)</br>
[http://127.0.0.1:8000/ddg?q=test](http://127.0.0.1:8000/ddg?q=test)

___
## 2) Docker-compose
**clone**
```python3
git clone https://github.com/deedy5/duckduckgo_search_api.git
cd duckduckgo_search_api
```

**run**
```python3
docker-compose up
```

**check**</br>
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)</br>
[http://127.0.0.1:8000/ddg?q=test](http://127.0.0.1:8000/ddg?q=test)

___
## 3) Docker
**clone**
```python3
git clone https://github.com/deedy5/duckduckgo_search_api.git
cd duckduckgo_search_api
```

**build**
```python3
docker build -t duckduckgo_search .
```

**run**
```python3
docker run -d --name ddg -p 8000:8000 duckduckgo_search
```
or
```python3
docker run -d --network host --name ddg -p 8000:8000 duckduckgo_search
```

**check**</br>
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)</br>
[http://127.0.0.1:8000/ddg?q=test](http://127.0.0.1:8000/ddg?q=test)

___
## 4) Test
```python3
python -m pytest
```
