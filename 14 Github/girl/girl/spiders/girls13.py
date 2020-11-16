# -*- coding: utf-8 -*-
import scrapy
from ..items import GirlItem
from scrapy_splash import SplashRequest

script = """
function main(splash, args)
  splash.images_enable = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  return {
    html = splash:html(),
  }
end
"""

class Girls13Spider(scrapy.Spider):
    name = 'girls13'
    allowed_domains = ['girl13.com']
    start_urls = ['http://www.girl13.com/page/1/']

    def parse(self, response):
        item = GirlItem()
        item['title'] = response.xpath('//li[@class="current"]/a/@href').get()
        item['img_list'] = response.xpath('//div[@class="waterfall_column"]/div/div/a/@href').getall()
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        yield item
        yield SplashRequest(next_page, self.parse, args={'lua_source': script, 'wait': 2})
