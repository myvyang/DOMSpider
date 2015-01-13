#!/usr/bin/env python

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class UrlsSpider(CrawlSpider):
    name = "urls"
    allowed_domains = ['seu.edu.cn']
    start_urls = [
        "http://www.seu.edu.cn"
    ]
    store_file = "store"

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow = True),
    )

    def parse_item(self, response):
        with open("store", "a+") as f:
            for url in response.xpath('//a/@href'):
                #print '---> ', url
                f.write(url.extract().encode('utf-8') + '\n')



