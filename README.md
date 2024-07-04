# Duckduckgo_search_api

Deploy an API that pulls data from duckduckgo search engine.

## Usage
clone
```python3
git clone https://github.com/deedy5/duckduckgo_search_api.git
cd duckduckgo_search_api
```
[Optional] set PROXY and TIMEOUT in main.py (*example with [iproyal residential proxies](https://iproyal.com?r=residential_proxies)*)
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
**check**</br>
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)</br>
[http://127.0.0.1:8000/text?q=test&max_results=5](http://127.0.0.1:8000/text?q=test&max_results=5)

## Disclaimer

This library is not affiliated with DuckDuckGo and is for educational purposes only. It is not intended for commercial use or any purpose that violates DuckDuckGo's Terms of Service. By using this library, you acknowledge that you will not use it in a way that infringes on DuckDuckGo's terms. The official DuckDuckGo website can be found at https://duckduckgo.com.
