"""
run the scrape bot from inside the project
using an exported function from this module.
"""

__all__ = ['run']


from scrapy.crawler import CrawlerProcess
from .spiders import JobScraperSpider


def run(url):
    process = CrawlerProcess({
        'USER_AGENT': 'AppleWebKit/537.36 (KHTML, like Gecko)'
    })
    process.crawl(JobScraperSpider, start_urls=[url])
    process.start()
