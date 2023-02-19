import logging
from itertools import count

import scrapy

# v.platformTrust = lambda: None
from {{cookiecutter.package_name}}.request import GetJobRequest
from {{cookiecutter.package_name}}.state import State

log = logging.getLogger(__name__)


class Spider(scrapy.Spider):
    name = "{{cookiecutter.package_name}}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = State()

    def start_requests(self):
        start = 3472312310
        for i in range(0, 10000000):
            i = int(1.1**i)
            yield GetJobRequest(state=self.state, job_id=start - i)
            yield GetJobRequest(state=self.state, job_id=start + i)
