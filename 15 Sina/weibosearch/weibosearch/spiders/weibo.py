# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    search_url = 'https://weibo.cn/search/mblog?hideSearchFrame='
    max_page = 10

    # https://weibo.cn/search/mblog?hideSearchFrame=&keyword=qwq
    def start_requests(self):
        keyword = 'qwq'
        url = '{url}&keyword={keyword}'.format(url=self.search_url, keyword=keyword)
        for page in range(self.max_page + 1):
            data = {
                'mp': str(self.max_page),
                'page': str(page)
            }
            yield FormRequest(url, callback=self.parse, formdata=data)

    def parse(self, response):
        print(response.url)
