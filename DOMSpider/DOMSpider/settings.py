# -*- coding: utf-8 -*-

# Scrapy settings for DOMSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'DOMSpider'

DOWNLOADER_MIDDLEWARES = {
    'DOMSpider.downloader.WebkitDownloader': 1000,
}

SPIDER_MODULES = ['DOMSpider.spiders']
NEWSPIDER_MODULE = 'DOMSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DOMSpider (+http://www.yourdomain.com)'
