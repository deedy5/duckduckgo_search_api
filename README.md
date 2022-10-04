#  duckduckgo_search_api
Example:

a) main page - https://ddg.deedy5.repl.co

b) news query - https://ddg.deedy5.repl.co/ddg_news?q=tesla&time=d&max_results=100
## 1) Usage
**run**
```python3
git clone https://github.com/deedy5/duckduckgo_search_api.git
cd duckduckgo_search_api
python start.py
```
___
**check**</br>
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)</br>
[http://127.0.0.1:8000/ddg?q=test](http://127.0.0.1:8000/ddg?q=test)

___
**test**
```python3
python -m pytest
```
___
## 2) Docker
**build**
```python3
git clone https://github.com/deedy5/duckduckgo_search_api.git
cd duckduckgo_search_api
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
