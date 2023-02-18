import os

import click
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from template_python_test_repo import spider


@click.command()
def main():
    os.environ["SCRAPY_SETTINGS_MODULE"] = "template_python_test_repo.settings"
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(spider.Spider)
    process.start()


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
# 3 455 725 343