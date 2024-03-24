#  duckduckgo_search_api

Deploy an API that pulls data from duckduckgo search engine.
___
## 1) Usage
**clone**
```python3
git clone https://github.com/deedy5/duckduckgo_search_api.git
cd duckduckgo_search_api
```
**add PROXY and set TIMEOUT in main.py** (*example with [iproyal residential proxies](https://iproyal.com?r=residential_proxies)*)
```python3
...
TIMEOUT = 20
PROXY = "socks5://user:password@geo.iproyal.com:32325"
...
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
**run**
```python3
docker-compose up --build
```
___
## 3) Docker
```python3
# build
docker build -t ddgs .
# run
docker run -d --name ddgs -p 8000:8000 --dns 1.1.1.1 --dns 8.8.8.8 ddgs
```
___
## 4) Test
```python3
python -m pytest
```
