import logging
import re
from datetime import datetime
from pathlib import Path

import attr
import rootpath
import scrapy

from template_python_test_repo import middlewares
from template_python_test_repo.state import State

log = logging.getLogger(__name__)

URL = "https://www.linkedin.com/graph"
MAX_PAGE = 999
ROOT_PATH = Path(rootpath.detect(__file__))


class RequestBase(scrapy.Request):
    def __str__(self):
        d = attr.asdict(self)
        d.pop("state")
        d_str = " ".join(f"{k}={v}" for k, v in d.items() if v is not None)
        return f"{self.__class__.__name__}({d_str})"

    __repr__ = __str__


dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


@attr.define(eq=False)
class GetJobRequest(RequestBase):
    state: State
    job_id: int

    def __attrs_post_init__(self):
        url = f"https://www.linkedin.com/voyager/api/jobs/jobPostings/{self.job_id}?decorationId=com.linkedin.voyager.deco.jobs.web.shared.WebFullJobPosting-65&topN=1&topNRequestedFlavors=List(TOP_APPLICANT,IN_NETWORK,COMPANY_RECRUIT,SCHOOL_RECRUIT,HIDDEN_GEM,ACTIVELY_HIRING_COMPANY)"
        super().__init__(url=url, callback=self.parse, headers=self.state.headers, errback=self._on_error)

        self.path = (ROOT_PATH / f"results/{dt_str}")
        self.path.mkdir(parents=True, exist_ok=True)

    def parse(self, response: scrapy.http.Response):
        (self.path / f"{self.job_id}.json").write_text(response.text)
        with (self.path / "ids.csv").open(mode="a") as f:
            f.write(f"{self.job_id}, {response.status}\n")
    def _on_error(self, failure):
        # middlewares.errback
        with (self.path / "ids.csv").open(mode="a") as f:
            f.write(f"{self.job_id}, {failure.value.response.status}\n")
