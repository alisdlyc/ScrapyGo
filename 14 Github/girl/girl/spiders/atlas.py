# -*- coding: utf-8 -*-
import scrapy
from ..items import GirlItem


class AtlasSpider(scrapy.Spider):
    name = 'atlas'
    allowed_domains = ['girl-atlas.net']
    start_urls = ['http://girl-atlas.net/']

    # http://girl-atlas.net/?p=2
    # http://girl-atlas.net  /album/576545f958e039318beb3f20
    # /album/576545f958e039318beb3f20

    def parse(self, response):
        set_urls = response.xpath('//div[@class="album-item row"]/div/h2/a/@href').getall()
        set_title = response.xpath('//div[@class="album-item row"]/div/h2/a/text()').getall()
        next_page = 'http://girl-atlas.net/%s' % response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()

        for t, u in zip(set_title, set_urls):
            yield scrapy.Request(url='http://girl-atlas.net%s' % u, callback=self.parse_pics, meta={'title': t})
        yield scrapy.Request(next_page, self.parse)

    def parse_pics(self, response):
        item = GirlItem()
        item['title'] = response.meta['title']
        item['img_list'] = response.xpath(
            '//ul[@class="slideview"]/li/img/@src | //ul[@class="slideview"]/li/img/@delay').getall()
        yield item
