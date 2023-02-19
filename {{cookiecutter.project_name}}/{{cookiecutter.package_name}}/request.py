import logging
from pathlib import Path

import attr
import rootpath
import scrapy

from {{cookiecutter.package_name}}.middlewares import errback
from {{cookiecutter.package_name}}.state import State

ROOT_PATH = Path(rootpath.detect(__file__))
logger = logging.getLogger(__name__)


class RequestBase(scrapy.Request):
    def __str__(self):
        d = attr.asdict(self)
        d.pop("state")
        d_str = " ".join(f"{k}={v}" for k, v in d.items() if v is not None)
        return f"{self.__class__.__name__}({d_str})"

    __repr__ = __str__


@attr.define(eq=False)
class DestinationRequest(RequestBase):
    state: State
    query: str

    def __attrs_post_init__(self):
        url = f"https://www.onlinetours.ru/api/v1/destinations?query={self.query}"
        logger.debug("New request url=%s", url)
        super().__init__(
            url=url, callback=self.parse, headers=self.state.headers, errback=errback
        )

    def parse(self, response: scrapy.http.Response):
        for item in response.json():
            yield item
