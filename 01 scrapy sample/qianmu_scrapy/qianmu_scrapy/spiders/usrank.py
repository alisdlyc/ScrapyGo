# -*- coding: utf-8 -*-
import scrapy

from ..items import RankListItem


class UsrankSpider(scrapy.Spider):
    name = 'usrank'
    # 允许爬取的域名 防止爬取了外链
    # 可以填根域名 这样可以爬取整个网站
    allowed_domains = ['www.qianmu.org']
    # 爬虫的入口地址，可以填入多个地址
    start_urls = ['http://www.qianmu.org/2019QS%E5%95%86%E7%A7%91%E4%B8%8E%E7%AE%A1%E7%90%86%E6%8E%92%E5%90%8D']

    # 当框架请求start_urls内的链接成功之后 会自动调用该方法
    def parse(self, response):
        # 解析网页 抽取网页中的所有链接 生成 links 列表
        # extract 方法返回的数据为列表，即使只有一个数据，所以只有一个数据时 使用 extract_first
        links = response.xpath('//div["rankItem"]//tbody/tr[position()>1]/td[2]//a/@href').extract()
        for link in links:
            if not link.startswith('http://www.qianmu.org'):
                link = 'http://www.qianmu.org/%s' % link
            # 让框架继续跟随link 再次发送请求到 link
            # 请求成功之后会调用 指定的callback 函数，即 self.parse_url
            yield response.follow(link, self.parse_url)

    def parse_url(self, response):
        response = response.replace(body=response.text.replace('\t', '').replace('\r\n', ''))
        # 将大学的信息按照name 包装成为一个字典
        item = RankListItem()
        item = {'name': response.xpath('//div["@wikiContent"]/h1["wikiTitle"][1]/text()').extract_first()}
        data = {}
        # data = {'name': response.xpath('//div["@wikiContent"]/h1["wikiTitle"][1]/text()')[0]}
        keys = response.xpath('//div[@class="infobox"]/table[1]//tr/td[1]/p/text()').extract()
        cols = response.xpath('//div[@class="infobox"]/table[1]//tr/td[2]')
        # 确定解析出来的数据只有一个时 可以使用 extract_first() 直接提取内容
        values = [' '.join(col.xpath('.//text()').extract_first()) for col in cols]
        # values = [' '.join(col.xpath('.//text()').extract) for col in cols]
        if (len(keys) == len(values)):
            data.update(zip(keys, values))
        # yield 出去的数据 会被框架接收 进行后续的处理
        # 如果没有进行处理 yield 会默认将数据打印到控制台

        item['rank'] = data.get('排名')
        item['country'] = data.get('国家')
        item['state'] = data.get('州省')
        item['city'] = data.get('城市')
        item['postgraduate'] = data.get('研究生人数')
        item['website'] = data.get('网址')
        print(item)
        yield item