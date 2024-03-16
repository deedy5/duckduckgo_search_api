from litestar.status_codes import HTTP_200_OK
from litestar.testing import TestClient

from duckduckgo_search_api.main import app


def test_text():
    with TestClient(app=app) as client:
        response = client.get("/text?q=usa")
        assert response.status_code == HTTP_200_OK
        assert len(response.json()) > 10


def test_images():
    with TestClient(app=app) as client:
        response = client.get("/images?q=usa")
        assert response.status_code == HTTP_200_OK
        assert len(response.json()) > 10


def test_videos():
    with TestClient(app=app) as client:
        response = client.get("/videos?q=usa")
        assert response.status_code == HTTP_200_OK
        assert len(response.json()) > 10


def test_news():
    with TestClient(app=app) as client:
        response = client.get("/news?q=usa")
        assert response.status_code == HTTP_200_OK
        assert len(response.json()) > 10
