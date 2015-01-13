#!/usr/bin/env python

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class UrlsSpider(CrawlSpider):
    name = "urls"
    allowed_domains = ['taobao.com']
    start_urls = [
        "http://www.taobao.com"
    ]

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow = True),
    )

    def parse_item(self, response):

        store_file = "taobao.store"

        with open(store_file, "a+") as f:
            f.write(response.url.encode('utf-8') + '\n')
            #for url in response.xpath('//a/@href'):
                #print '---> ', url
            #    f.write(url.extract().encode('utf-8') + '\n')



