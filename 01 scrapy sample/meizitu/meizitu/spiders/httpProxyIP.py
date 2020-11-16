# -*- coding: utf-8 -*-
import scrapy


class HttpproxyipSpider(scrapy.Spider):
    name = 'httpProxyIP'
    allowed_domains = ['icanhazip.com']
    start_urls = ['http://icanhazip.com/']

    def parse(self, response):
        print(response.text)
