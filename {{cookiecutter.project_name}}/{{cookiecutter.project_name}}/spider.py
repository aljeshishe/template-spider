import scrapy

from {{cookiecutter.project_name}}.request import DestinationRequest
from {{cookiecutter.project_name}}.state import State


class Spider(scrapy.Spider):
    name = "{{cookiecutter.project_name}}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = State()

    def start_requests(self):
        yield DestinationRequest(state=self.state, query="турц")

    def parse(self, response: scrapy.http.Response, **kwargs):
        raise NotImplementedError
