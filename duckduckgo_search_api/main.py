import logging
from typing import Annotated

import uvicorn
from duckduckgo_search import AsyncDDGS
from fastapi import FastAPI, Query
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel

__version__ = "0.7.0"


TIMEOUT = 10
PROXY = None

app = FastAPI(
    title="duckduckgo_search_api",
    description="Search for text, images, videos, news",
    version=__version__,
    redoc_url="/",
    docs_url=None,
    default_response_class=ORJSONResponse,
)
app.add_middleware(GZipMiddleware, minimum_size=1000)


class DdgTextOut(BaseModel):
    title: str
    href: str
    body: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Google",
                    "href": "https://www.google.com",
                    "body": "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
                }
            ],
        }
    }


class DdgImagesOut(BaseModel):
    title: str
    image: str
    thumbnail: str
    url: str
    height: int
    width: int
    source: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Enjoying The Apple Harvest :: 100+ Apple Recipes! • The Prairie Homestead",
                    "image": "https://www.theprairiehomestead.com/wp-content/uploads/2014/10/150.jpg",
                    "thumbnail": "https://tse1.mm.bing.net/th?id=OIP.C0I3WQo6IJ2XehGprhMujQHaLI&pid=Api",
                    "url": "https://www.theprairiehomestead.com/2014/10/100-apple-recipes.html/attachment/150",
                    "height": 3008,
                    "width": 2000,
                    "source": "Bing",
                }
            ],
        }
    }


class DdgVideosOut(BaseModel):
    content: str
    description: str
    duration: str
    embed_html: str
    embed_url: str
    images: dict
    provider: str
    published: str
    publisher: str
    statistics: dict
    title: str
    uploader: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "content": "https://www.youtube.com/watch?v=kp9vGSTqWvI",
                "description": "The Fall Of The Soviet Union https://www.youtube.com/watch?v=zadkWw702_M&t=5s » Subscribe to NowThis World: http://go.nowth.is/World_Subscribe Until its fall in 1991, the Soviet Union was a major player on the world stage. So just how did the USSR come to be? Learn More: The New York Times: Nov. 7, 1917 | Russian Government Overthrown in ...",
                "duration": "4:32",
                "embed_html": '<iframe width="1280" height="720" src="https://www.youtube.com/embed/kp9vGSTqWvI?autoplay=1" frameborder="0" allowfullscreen></iframe>',
                "embed_url": "https://www.youtube.com/embed/kp9vGSTqWvI?autoplay=1",
                "images": {
                    "large": "https://tse2.mm.bing.net/th?id=OVP._E2Er8OwgQriFRpyXV21YgIIEk&pid=Api",
                    "medium": "https://tse2.mm.bing.net/th?id=OVP._E2Er8OwgQriFRpyXV21YgIIEk&pid=Api",
                    "motion": "https://tse4.mm.bing.net/th?id=OM.usQE_OeDp6mYXw_1645416058&pid=Api",
                    "small": "https://tse2.mm.bing.net/th?id=OVP._E2Er8OwgQriFRpyXV21YgIIEk&pid=Api",
                },
                "provider": "Bing",
                "published": "2017-01-08T13:00:04.0000000",
                "publisher": "YouTube",
                "statistics": {"viewCount": 720253},
                "title": "The Rise Of The Soviet Union",
                "uploader": "NowThis World",
            },
        }
    }


class DdgNewsOut(BaseModel):
    date: str
    title: str
    body: str
    url: str
    image: str | None = None
    source: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "date": "2022-06-16T18:14:00",
                "title": "Ford recalls 394,000 vehicles in Canada over rollaway concerns",
                "body": "Ford is recalling more than 3.3 million vehicles in North America, including 394,000 in Canada, that could roll away because a damaged or missing part may prevent the vehicle from shifting into the intended gear.",
                "url": "https://canada.autonews.com/recalls/ford-recalls-394000-vehicles-canada-over-rollaway-concerns",
                "image": "https://s3-prod-canada.autonews.com/s3fs-public/styles/1200x630/public/Ford%20badge%20web.jpg",
                "source": "Automotive News",
            },
        }
    }


@app.get("/text")
async def ddg_search(
    q: Annotated[str, Query(description="Query string")],
    region: Annotated[
        str, Query(description="wt-wt, us-en, uk-en, ru-ru, etc.")
    ] = "wt-wt",
    safesearch: Annotated[str, Query(description="on, moderate, off")] = "moderate",
    timelimit: Annotated[str | None, Query(description="d, w, m, y")] = None,
    backend: Annotated[str, Query(description="api, html, lite")] = "api",
    max_results: Annotated[
        int | None, Query(description="number or results, max=200")
    ] = None,
) -> list[DdgTextOut]:
    """DuckDuckGo text search. Query params: https://duckduckgo.com/params"""
    try:
        async with AsyncDDGS(proxies=PROXY, timeout=TIMEOUT) as ddgs:
            results = await ddgs.text(
                q,
                region,
                safesearch,
                timelimit,
                backend,
                max_results,
            )
            return results
    except Exception as ex:
        logging.warning(ex)


@app.get("/images")
async def ddg_images_search(
    q: Annotated[str, Query(description="Query string")],
    region: Annotated[
        str | None, Query(description="wt-wt, us-en, uk-en, ru-ru, etc.")
    ] = "wt-wt",
    safesearch: Annotated[
        str | None, Query(description="on, moderate, off")
    ] = "moderate",
    timelimit: Annotated[
        str | None, Query(description="Day, Week, Month, Year")
    ] = None,
    size: Annotated[
        str | None, Query(description="Small, Medium, Large, Wallpaper")
    ] = None,
    color: Annotated[
        str | None,
        Query(
            description="""color, Monochrome, Red, Orange, Yellow, Green, Blue,
            Purple, Pink, Brown, Black, Gray, Teal, White.""",
        ),
    ] = None,
    type_image: Annotated[
        str | None, Query(description="photo, clipart, gif, transparent, line")
    ] = None,
    layout: Annotated[str | None, Query(description="Square, Tall, Wide")] = None,
    license_image: Annotated[
        str | None,
        Query(
            description="""any (All Creative Commons), Public (PublicDomain),
            Share (Free to Share and Use), ShareCommercially (Free to Share and Use Commercially),
            Modify (Free to Modify, Share, and Use), ModifyCommercially (Free to Modify, Share, and
            Use Commercially)""",
        ),
    ] = None,
    max_results: Annotated[
        int | None, Query(description="number of results, max=1000")
    ] = None,
) -> list[DdgImagesOut]:
    """DuckDuckGo images search."""

    try:
        async with AsyncDDGS(proxies=PROXY, timeout=TIMEOUT) as ddgs:
            results = await ddgs.images(
                q,
                region,
                safesearch,
                timelimit,
                size,
                color,
                type_image,
                layout,
                license_image,
                max_results,
            )
            return results
    except Exception as ex:
        logging.warning(ex)


@app.get("/videos")
async def ddg_videos_search(
    q: Annotated[str, Query(description="Query string")],
    region: Annotated[
        str | None, Query(description="country - wt-wt, us-en, uk-en, ru-ru, etc.")
    ] = "wt-wt",
    safesearch: Annotated[
        str | None, Query(description="on, moderate, off")
    ] = "moderate",
    timelimit: Annotated[str | None, Query(description="d, w, m")] = None,
    resolution: Annotated[str | None, Query(description="high, standard")] = None,
    duration: Annotated[str | None, Query(description="short, medium, long")] = None,
    license_videos: Annotated[
        str | None, Query(description="creativeCommon, youtube")
    ] = None,
    max_results: Annotated[
        int | None, Query(description="number of results, max=1000")
    ] = None,
) -> list[DdgVideosOut]:
    """DuckDuckGo videos search."""

    try:
        async with AsyncDDGS(proxies=PROXY, timeout=TIMEOUT) as ddgs:
            results = await ddgs.videos(
                q,
                region,
                safesearch,
                timelimit,
                resolution,
                duration,
                license_videos,
                max_results,
            )
            return results
    except Exception as ex:
        logging.warning(ex)


@app.get("/news")
async def ddg_news_search(
    q: Annotated[str, Query(description="Query string")],
    region: Annotated[
        str | None, Query(description="country - wt-wt, us-en, uk-en, ru-ru, etc.")
    ] = "wt-wt",
    safesearch: Annotated[
        str | None, Query(description="on, moderate, off")
    ] = "moderate",
    timelimit: Annotated[str | None, Query(description="d, w, m")] = None,
    max_results: Annotated[
        int | None, Query(description="number of results, max=240")
    ] = None,
) -> list[DdgNewsOut]:
    """DuckDuckGo news search"""

    try:
        async with AsyncDDGS(proxies=PROXY, timeout=TIMEOUT) as ddgs:
            results = await ddgs.news(
                q,
                region,
                safesearch,
                timelimit,
                max_results,
            )
            return results
    except Exception as ex:
        logging.warning(ex)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
