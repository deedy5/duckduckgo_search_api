import logging
from dataclasses import dataclass
from typing import Annotated, cast

import uvicorn
from duckduckgo_search import DDGS
from litestar import Litestar, Response, get
from litestar.config.compression import CompressionConfig
from litestar.openapi import OpenAPIConfig, OpenAPIController
from litestar.params import Parameter
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR

__version__ = "0.10.0"


TIMEOUT = 10
PROXY: dict[str, str] | str | None = None


@dataclass
class DdgTextOut:
    title: str
    href: str
    body: str


@dataclass
class DdgImagesOut:
    title: str
    image: str
    thumbnail: str
    url: str
    height: int
    width: int
    source: str


@dataclass
class DdgVideosOut:
    content: str
    description: str
    duration: str
    embed_html: str
    embed_url: str
    images: dict[str, str]
    provider: str
    published: str
    publisher: str
    statistics: dict[str, int]
    title: str
    uploader: str


@dataclass
class DdgNewsOut:
    date: str
    title: str
    body: str
    url: str
    source: str
    image: str


class MyOpenAPIController(OpenAPIController):
    path = "/"


@get("/text", sync_to_thread=True)
def ddg_text_search(
    q: Annotated[str, Parameter(description="Search query", required=True)],
    region: Annotated[str, Parameter(description="Region", default="wt-wt")] = "wt-wt",
    safesearch: Annotated[
        str,
        Parameter(
            description="Safe search",
            default="moderate",
            pattern="^(off|moderate|strict)$",
        ),
    ] = "moderate",
    timelimit: Annotated[
        str | None,
        Parameter(description="Time limit", default=None, pattern="^(d|w|m|y)$"),
    ] = None,
    backend: Annotated[
        str,
        Parameter(description="Backend", default="auto", pattern="^(auto|html|lite)$"),
    ] = "auto",
    max_results: Annotated[
        int | None,
        Parameter(title="max_results", description="Max results. Max 100", default=None),
    ] = None,
) -> list[DdgTextOut]:
    """DuckDuckGo text search. Query params: https://duckduckgo.com/params"""
    try:
        ddgs = DDGS(proxies=PROXY, timeout=TIMEOUT)
        results = ddgs.text(
            q,
            region=region,
            safesearch=safesearch,
            timelimit=timelimit,
            backend=backend,
            max_results=max_results,
        )
        return cast(list[DdgTextOut], results)
    except Exception as ex:
        logging.warning(ex)
        return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)  # type: ignore


@get("/images", sync_to_thread=True)
def ddg_images_search(
    q: Annotated[str, Parameter(description="Search query", required=True)],
    region: Annotated[str, Parameter(description="Region", default="wt-wt")] = "wt-wt",
    safesearch: Annotated[
        str,
        Parameter(
            description="Safe search",
            default="moderate",
            pattern="^(off|moderate|strict)$",
        ),
    ] = "moderate",
    timelimit: Annotated[
        str | None,
        Parameter(description="Time limit", default=None, pattern="^(Day|Week|Month|Year)$"),
    ] = None,
    size: Annotated[
        str | None,
        Parameter(description="size", default=None, pattern="^(Small|Medium|Large|Wallpaper)$"),
    ] = None,
    color: Annotated[
        str | None,
        Parameter(
            description="color",
            default=None,
            pattern="^(color|Monochrome|Red|Orange|Yellow|Green|Blue|Purple|Pink|Brown|Black|Gray|Teal|White)$",
        ),
    ] = None,
    type_image: Annotated[
        str | None,
        Parameter(
            description="type of image",
            default=None,
            pattern="^(photo|clipart|gif|transparent|line)$",
        ),
    ] = None,
    layout: Annotated[
        str | None,
        Parameter(description="layout", default=None, pattern="^(Square|Tall|Wide)$"),
    ] = None,
    license_image: Annotated[
        str | None,
        Parameter(
            description="""license of image: any (All Creative Commons), Public (PublicDomain),
            Share (Free to Share and Use), ShareCommercially (Free to Share and Use Commercially),
            Modify (Free to Modify, Share, and Use), ModifyCommercially (Free to Modify, Share, and
            Use Commercially)""",
            default=None,
            pattern="^(any|Public|Share|ShareCommercially|Modify|ModifyCommercially)$",
        ),
    ] = None,
    max_results: Annotated[
        int | None,
        Parameter(title="max_results", description="Max results. Max 500", default=None),
    ] = None,
) -> list[DdgImagesOut]:
    """DuckDuckGo images search."""
    try:
        ddgs = DDGS(proxies=PROXY, timeout=TIMEOUT)
        results = ddgs.images(
            q,
            region=region,
            safesearch=safesearch,
            timelimit=timelimit,
            size=size,
            color=color,
            type_image=type_image,
            layout=layout,
            license_image=license_image,
            max_results=max_results,
        )
        return cast(list[DdgImagesOut], results)
    except Exception as ex:
        logging.warning(ex)
        return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)  # type: ignore


@get("/videos", sync_to_thread=True)
def ddg_videos_search(
    q: Annotated[str, Parameter(description="Search query", required=True)],
    region: Annotated[str, Parameter(description="Region", default="wt-wt")] = "wt-wt",
    safesearch: Annotated[
        str,
        Parameter(
            description="Safe search",
            default="moderate",
            pattern="^(off|moderate|strict)$",
        ),
    ] = "moderate",
    timelimit: Annotated[
        str | None,
        Parameter(description="Time limit", default=None, pattern="^(d|w|m)$"),
    ] = None,
    resolution: Annotated[
        str | None,
        Parameter(description="Resolution", default=None, pattern="^(high|standard)$"),
    ] = None,
    duration: Annotated[
        str | None,
        Parameter(description="Duration", default=None, pattern="^(short|medium|long)$"),
    ] = None,
    license_videos: Annotated[
        str | None,
        Parameter(description="License of videos", default=None, pattern="^(creativeCommon|youtube)$"),
    ] = None,
    max_results: Annotated[
        int | None,
        Parameter(title="max_results", description="Max results. Max 400", default=None),
    ] = None,
) -> list[DdgVideosOut]:
    """DuckDuckGo videos search."""
    try:
        ddgs = DDGS(proxies=PROXY, timeout=TIMEOUT)
        results = ddgs.videos(
            q,
            region,
            safesearch,
            timelimit,
            resolution,
            duration,
            license_videos,
            max_results,
        )
        return cast(list[DdgVideosOut], results)
    except Exception as ex:
        logging.warning(ex)
        return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)  # type: ignore


@get("/news", sync_to_thread=True)
def ddg_news_search(
    q: Annotated[str, Parameter(description="Search query", required=True)],
    region: Annotated[str, Parameter(description="Region", default="wt-wt")] = "wt-wt",
    safesearch: Annotated[
        str,
        Parameter(
            description="Safe search",
            default="moderate",
            pattern="^(off|moderate|strict)$",
        ),
    ] = "moderate",
    timelimit: Annotated[
        str | None,
        Parameter(description="Time limit", default=None, pattern="^(d|w|m)$"),
    ] = None,
    max_results: Annotated[
        int | None,
        Parameter(title="max_results", description="Max results. Max 200", default=None),
    ] = None,
) -> list[DdgNewsOut]:
    """DuckDuckGo news search"""
    try:
        ddgs = DDGS(proxies=PROXY, timeout=TIMEOUT)
        results = ddgs.news(
            q,
            region,
            safesearch,
            timelimit,
            max_results,
        )
        return cast(list[DdgNewsOut], results)
    except Exception as ex:
        logging.warning(ex)
        return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)  # type: ignore


app = Litestar(
    route_handlers=[
        ddg_text_search,
        ddg_images_search,
        ddg_videos_search,
        ddg_news_search,
    ],
    compression_config=CompressionConfig(
        backend="gzip",
        gzip_compress_level=1,
    ),
    openapi_config=OpenAPIConfig(
        title="duckduckgo_search_api", version=__version__, openapi_controller=MyOpenAPIController
    ),
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
