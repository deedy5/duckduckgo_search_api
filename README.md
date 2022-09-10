# Docker
1) build
```python3
docker image build -t duckduckgo_search .
```

2) run
```python3
docker run -d --name ddg -p 8000:8000 duckduckgo_search
```

3) check</br>
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)</br>
[http://127.0.0.1:8000/ddg?q=test](http://127.0.0.1:8000/ddg?q=test)
___
