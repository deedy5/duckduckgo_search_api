# v0.3
___
# Usage
**run**
```python3
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
# Docker
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
