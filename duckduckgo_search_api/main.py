from typing import Dict, List, Optional

import uvicorn
from duckduckgo_search import ddg, ddg_images, ddg_news, ddg_videos
from fastapi import FastAPI, Query
from pydantic import BaseModel


__version__ = "0.1"


app = FastAPI(
    title="duckduckgo_search_api",
    description="Search for text, images, videos, news",
    version=__version__,
    redoc_url="/",
    docs_url=None,
)


class DdgIn(BaseModel):
    q: str
    region: Optional[str] = "wt-wt"
    safesearch: Optional[str] = "Moderate"
    time: Optional[str] = None
    max_results: Optional[int] = 28

    class Config:
        schema_extra = {
            "example": {
                "q": "Google",
                "region": "wt-wt",
                "safesearch": "Moderate",
                "time": "y",
                "max_results": 100,
            },
        }


class DdgOut(BaseModel):
    title: str
    href: str
    body: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Google",
                "href": "https://www.google.com",
                "body": "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
            },
        }


class DdgImagesIn(BaseModel):
    q: str
    region: Optional[str] = "wt-wt"
    safesearch: Optional[str] = "Moderate"
    time: Optional[str] = None
    size: Optional[str] = None
    color: Optional[str] = None
    type_image: Optional[str] = None
    layout: Optional[str] = None
    license_image: Optional[str] = None
    max_results: Optional[int] = 100

    class Config:
        schema_extra = {
            "example": {
                "q": "apple",
                "region": "wt-wt",
                "safesearch": "Moderate",
                "time": "Year",
                "size": "Wallpaper",
                "color": "color",
                "type_image": "photo",
                "layout": "Wide",
                "license_image": "any",
                "max_results": 100,
            },
        }


class DdgImagesOut(BaseModel):
    title: str
    image: str
    thumbnail: str
    url: str
    height: str
    width: str
    source: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Enjoying The Apple Harvest :: 100+ Apple Recipes! • The Prairie Homestead",
                "image": "https://www.theprairiehomestead.com/wp-content/uploads/2014/10/150.jpg",
                "thumbnail": "https://tse1.mm.bing.net/th?id=OIP.C0I3WQo6IJ2XehGprhMujQHaLI&pid=Api",
                "url": "https://www.theprairiehomestead.com/2014/10/100-apple-recipes.html/attachment/150",
                "height": "3008",
                "width": "2000",
                "source": "Bing",
            },
        }


class DdgVideosIn(BaseModel):
    q: str
    region: Optional[str] = "wt-wt"
    safesearch: Optional[str] = "Moderate"
    time: Optional[str] = None
    resolution: Optional[str] = None
    duration: Optional[str] = None
    license_videos: Optional[str] = None
    max_results: Optional[int] = 62

    class Config:
        schema_extra = {
            "example": {
                "q": "USSR",
                "region": "wt-wt",
                "safesearch": "Moderate",
                "time": "y",
                "resolution": "high",
                "duration": "medium",
                "license_videos": "youtube",
                "max_results": 62,
            },
        }


class DdgVideosOut(BaseModel):
    content: str
    description: str
    duration: str
    embed_html: str
    embed_url: str
    images: Dict
    provider: str
    published: str
    publisher: str
    statistics: Dict
    title: str
    uploader: str

    class Config:
        schema_extra = {
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


class DdgNewsIn(BaseModel):
    q: str
    region: Optional[str] = "wt-wt"
    safesearch: Optional[str] = "Moderate"
    time: Optional[str] = None
    max_results: Optional[int] = 30

    class Config:
        schema_extra = {
            "example": {
                "q": "Ford",
                "region": "wt-wt",
                "safesearch": "Moderate",
                "time": "y",
                "max_results": 30,
            },
        }


class DdgNewsOut(BaseModel):
    date: str
    title: str
    body: str
    url: str
    image: Optional[str]
    source: str

    class Config:
        schema_extra = {
            "example": {
                "date": "2022-06-16T18:14:00",
                "title": "Ford recalls 394,000 vehicles in Canada over rollaway concerns",
                "body": "Ford is ecalling more than 3.3 million vehicles in North America, including 394,000 in Canada, that could roll away because a damaged or missing part may prevent the vehicle from shifting into the intended gear.",
                "url": "https://canada.autonews.com/recalls/ford-recalls-394000-vehicles-canada-over-rollaway-concerns",
                "image": "https://s3-prod-canada.autonews.com/s3fs-public/styles/1200x630/public/Ford%20badge%20web.jpg",
                "source": "Automotive News",
            },
        }


@app.get("/ddg", response_model=List[DdgOut])
def ddg_search(
    q: str = Query(description="Query string"),
    region: Optional[str] = Query(default="wt-wt", description="wt-wt, us-en, uk-en, ru-ru, etc."),
    safesearch: Optional[str] = Query(default="Moderate", description="On, Moderate, Off"),
    time: Optional[str] = Query(default="None", description="d, w, m, y"),
    max_results: Optional[int] = Query(default=28, description="number or results,, max=200")
):
    """DuckDuckGo text search. Query params: https://duckduckgo.com/params"""

    return ddg(q, region, safesearch, time, max_results)


@app.get("/ddg_images", response_model=List[DdgImagesOut])
def ddg_images_search(
    q: str = Query(description="Query string"),
    region: Optional[str] = Query(default="wt-wt", description="wt-wt, us-en, uk-en, ru-ru, etc."),
    safesearch: Optional[str] = Query(default="Moderate", description="On, Moderate, Off"),
    time: Optional[str] = Query(default=None, description="Day, Week, Month, Year"),
    size: Optional[str] = Query(default=None, description="Small, Medium, Large, Wallpaper"),
    color: Optional[str] = Query(default=None, description="""color, Monochrome, Red, Orange, Yellow, Green, Blue,
            Purple, Pink, Brown, Black, Gray, Teal, White."""),
    type_image: Optional[str] = Query(default=None, description="photo, clipart, gif, transparent, line"),
    layout: Optional[str] = Query(default=None, description="Square, Tall, Wide"),
    license_image: Optional[str] = Query(default=None, description="""any (All Creative Commons), Public (PublicDomain),
            Share (Free to Share and Use), ShareCommercially (Free to Share and Use Commercially),
            Modify (Free to Modify, Share, and Use), ModifyCommercially (Free to Modify, Share, and
            Use Commercially)"""),
    max_results: Optional[int] = Query(default=100, description="number of results, max=1000"),
):
    """DuckDuckGo images search."""

    return ddg_images(
        q,
        region,
        safesearch,
        time,
        size,
        color,
        type_image,
        layout,
        license_image,
        max_results,
    )

@app.get("/ddg_videos", response_model=List[DdgVideosOut])
def ddg_videos_search(
    q: str = Query(description="Query string"),
    region: Optional[str] = Query(default="wt-wt", description="country - wt-wt, us-en, uk-en, ru-ru, etc."),
    safesearch: Optional[str] = Query(default="Moderate", description="On, Moderate, Off"),
    time: Optional[str] = Query(default=None, description="d, w, m"),
    resolution: Optional[str] = Query(default=None, description="high, standart"),
    duration: Optional[str] = Query(default=None, description="short, medium, long"),
    license_videos: Optional[str] = Query(default=None, description="creativeCommon, youtube"),
    max_results: Optional[int] = Query(default=62, description="number of results, max=1000")
):
    """DuckDuckGo videos search."""

    return ddg_videos(
        q,
        region,
        safesearch,
        time,
        resolution,
        duration,
        license_videos,
        max_results,
    )


@app.get("/ddg_news", response_model=List[DdgNewsOut])
def ddg_news_search(
    q: str = Query(description="Query string"),
    region: Optional[str] = Query(default="wt-wt", description="country - wt-wt, us-en, uk-en, ru-ru, etc."),
    safesearch: Optional[str] = Query(default="Moderate", description="On, Moderate, Off"),
    time: Optional[str] = Query(default="None", description="d, w, m"),
    max_results: Optional[int] = Query(default=30, description="number or results, max=240"),
):
    """DuckDuckGo news search"""

    return ddg_news(q, region, safesearch, time, max_results)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
