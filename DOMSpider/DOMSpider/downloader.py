
from scrapy.http import Request, HtmlResponse

import jwebkit

max_sec = 1


class WebkitDownloader(object):

    def process_request(self, request, spider):
        htmlStr = jwebkit.get_page(request.url, max_sec)


        if not htmlStr:
            return None
        return HtmlResponse(request.url, body = htmlStr.encode('utf-8'))

