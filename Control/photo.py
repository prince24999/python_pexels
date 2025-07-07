from typing import List
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class Src:
    original: str
    large2x: str
    large: str
    medium: str
    small: str
    portrait: str
    landscape: str
    tiny: str

    @staticmethod
    def from_dict(obj: Any) -> "Src":
        _original = str(obj.get("original"))
        _large2x = str(obj.get("large2x"))
        _large = str(obj.get("large"))
        _medium = str(obj.get("medium"))
        _small = str(obj.get("small"))
        _portrait = str(obj.get("portrait"))
        _landscape = str(obj.get("landscape"))
        _tiny = str(obj.get("tiny"))
        return Src(
            _original, _large2x, _large, _medium, _small, _portrait, _landscape, _tiny
        )


@dataclass
class Photo:
    id: int
    width: int
    height: int
    url: str
    photographer: str
    photographer_url: str
    photographer_id: int
    avg_color: str
    src: Src
    liked: bool
    alt: str

    @staticmethod
    def from_dict(obj: Any) -> "Photo":
        _id = int(obj.get("id"))
        _width = int(obj.get("width"))
        _height = int(obj.get("height"))
        _url = str(obj.get("url"))
        _photographer = str(obj.get("photographer"))
        _photographer_url = str(obj.get("photographer_url"))
        _photographer_id = int(obj.get("photographer_id"))
        _avg_color = str(obj.get("avg_color"))
        _src = Src.from_dict(obj.get("src"))
        _liked = bool
        _alt = str(obj.get("alt"))
        return Photo(
            _id,
            _width,
            _height,
            _url,
            _photographer,
            _photographer_url,
            _photographer_id,
            _avg_color,
            _src,
            _liked,
            _alt,
        )


@dataclass
class Root:
    page: int
    per_page: int
    photos: List[Photo]
    total_results: int
    next_page: str

    @staticmethod
    def from_dict(obj: Any) -> "Root":
        _page = int(obj.get("page"))
        _per_page = int(obj.get("per_page"))
        _photos = [Photo.from_dict(y) for y in obj.get("photos")]
        _total_results = int(obj.get("total_results"))
        _next_page = str(obj.get("next_page"))
        return Root(_page, _per_page, _photos, _total_results, _next_page)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
