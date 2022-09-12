from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_ddg_search():
    response = client.get("/ddg?q=usa")
    assert response.status_code == 200
    assert len(response.json()) > 10


def test_ddg_images_search():
    response = client.get("/ddg_images?q=usa")
    assert response.status_code == 200
    assert len(response.json()) > 10


def test_ddg_videos_search():
    response = client.get("/ddg_videos?q=usa")
    assert response.status_code == 200
    assert len(response.json()) > 10


def test_ddg_news_search():
    response = client.get("/ddg_news?q=usa")
    assert response.status_code == 200
    assert len(response.json()) > 10
