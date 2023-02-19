"""Sample integration test module using pytest-describe and expecter."""

# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned
import json
import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from {{cookiecutter.project_name}} import spider


def test_ok(tmp_path):
    os.environ["SCRAPY_SETTINGS_MODULE"] = "{{cookiecutter.project_name}}.settings"
    settings = get_project_settings()
    path = tmp_path / "results.json"
    settings.set("FEEDS", {str(path): {"format": "json"}})
    process = CrawlerProcess(settings=settings)
    settings.getdict("FEEDS")
    process.crawl(spider.Spider)
    process.start()

    data = path.read_text(encoding="unicode_escape")
    assert "Турция" in data
    assert len(json.loads(data)) > 0
