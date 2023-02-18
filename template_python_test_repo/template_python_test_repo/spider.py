import logging
from itertools import count

import scrapy
# v.platformTrust = lambda: None
from template_python_test_repo.request import GetJobRequest

from template_python_test_repo.state import State

log = logging.getLogger(__name__)


class Spider(scrapy.Spider):
    name = "template_python_test_repo"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = State()

    def start_requests(self):
        start = 3472312310
        for i in range(0, 10000000):
            i = int(1.1**i)
            yield GetJobRequest(state=self.state, job_id=start-i)
            yield GetJobRequest(state=self.state, job_id=start+i)
