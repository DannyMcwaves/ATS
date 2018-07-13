# -*- coding: utf-8 -*-
import scrapy
import logging


class JobScraperSpider(scrapy.Spider):

    name = 'jobScraper'

    def __init__(self, *args, **kwargs):
        logging.getLogger('scrapy').setLevel(logging.CRITICAL)
        super(JobScraperSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        res = {
            'title': response.css('title::text').extract_first(),
            'url': response.url,
            'header': response.css('div.job-detail-header::text').extract(),
            'content': response.css('div.job-detail-content::text').extract(),
            'company': response.css('div.company-page::text').extract()
        }
        print(res)
        yield res
