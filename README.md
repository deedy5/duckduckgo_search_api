# Duckduckgo_search_api

Deploy an API that pulls data from duckduckgo search engine.

## Usage
### 1) Simple (pull from hub.docker.com)
```python3
docker run -p 8000:8000 deedy5/duckduckgo_search_api
```
**check**</br>
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)</br>
[http://127.0.0.1:8000/text?q=test&max_results=5](http://127.0.0.1:8000/text?q=test&max_results=5)

___
### 2) Advanced (build yourself)
clone
```python3
git clone https://github.com/deedy5/duckduckgo_search_api.git
cd duckduckgo_search_api
```
add PROXY and set TIMEOUT in main.py (*example with [iproyal residential proxies](https://iproyal.com?r=residential_proxies)*)
```python3
TIMEOUT = 20
PROXY = "socks5://user:password@geo.iproyal.com:32325"
```
create venv and install requirements
```python3
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```
build and run using `docker-compose`
```python3
docker-compose up --build
```
build and run using `docker`
```python3
docker build -t ddgs .
docker run -d --name ddgs -p 8000:8000 --dns 1.1.1.1 --dns 8.8.8.8 ddgs
```