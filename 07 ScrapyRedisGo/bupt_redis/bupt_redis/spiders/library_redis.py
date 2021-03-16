import re

import scrapy
import json
from jsonpath import jsonpath
from bupt_redis.items import BookItem

# 01、 导入分布式爬虫类
from scrapy_redis.spiders import RedisSpider


# 02、 继承分布式爬虫类
class LibraryRedisSpider(RedisSpider):
    name = 'library_redis'
    # 03、 注销start_urls和allowed_domains
    # allowed_domains = ['bupt.edu.cn']
    # start_urls = ['http://opac.bupt.edu.cn:8080/search-classify.html']
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'JSESSIONID=3044E621E5D2AF4195CB41E4DEAD87B2',
        'Referer': 'http://opac.bupt.edu.cn:8080/search-classify.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Host': 'opac.bupt.edu.cn:8080',
        'Origin': 'http://opac.bupt.edu.cn:8080'
    }

    # 04、 设置redis-key, 用于存储start_url
    redis_key = 'bupt'

    # 05、 设置 __init__
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(LibraryRedisSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        classifications = response.xpath('//div[@class="panel-group"]/div[@class="book-menu" and @role="tab"]')
        for classification in classifications:
            # item = BookItem()
            # item['first_heading'] = classification.xpath('./span[2]/text()')
            seconds = classification.xpath('./following-sibling::div[1]/div')
            second_headings = seconds.xpath('./span[1]')

            for second_heading in second_headings:
                # item['second_heading'] = second_heading.xpath('./../span[last()]/text()').get()
                thirds = second_heading.xpath('./../following-sibling::div[1]/div')

                for third in thirds:
                    # item = BookItem()
                    # item['classno'] = third.xpath('./span[1]/text()').extract_first()
                    # item['heading'] = third.xpath('./span[last()]/text()')
                    # print(third.xpath('./span[1]/text()').extract_first().replace(' ', ''))

                    yield scrapy.FormRequest(
                        url='http://opac.bupt.edu.cn:8080//search-classify.json',
                        headers=self.headers,
                        formdata=dict(
                            # classnoAbs=item['classno'],
                            classnoAbs=third.xpath('./span[1]/text()').extract_first().replace(' ', ''),
                            pageNo='0',
                            pageSize='10',
                            order='-1',
                        ),
                        callback=self.parse_books_pages,
                        meta={'Abs': third.xpath('./span[1]/text()').extract_first().replace(' ', ''),
                              'Heading': third.xpath('./span[last()]/text()').extract_first(), }
                    )

    # 解析当前标签共有多少页
    def parse_books_pages(self, response):
        Abs = response.meta['Abs']
        Heading = response.meta['Heading']
        response = re.sub(r"[\x00-\x08]|[\x0B-\x0C]|[\x0E-\x1F]", '', response.text)

        # print('%s have %d pages' % (Abs, jsonpath(json.loads(response), '$..totalPage')[0]))
        for _ in range(jsonpath(json.loads(response), '$..totalPage')[0] + 1):
            yield scrapy.FormRequest(
                url='http://opac.bupt.edu.cn:8080//search-classify.json',
                headers=self.headers,
                formdata=dict(
                    # classnoAbs=item['classno'],
                    classnoAbs=Abs,
                    pageNo='%d' % _,
                    pageSize='10',
                    order='-1',
                ),
                callback=self.get_books_data,
                meta={'Abs': Abs,
                      'Heading': Heading},
                dont_filter=True
            )

    def get_books_data(self, response):
        Abs = response.meta['Abs']
        Heading = response.meta['Heading']
        response = re.sub(r"[\x00-\x08]|[\x0B-\x0C]|[\x0E-\x1F]", '', response.text)
        books = json.loads(response)['data']
        for book in books:
            item = BookItem()
            item['heading'] = Heading
            item['classno'] = Abs
            for field in item.fields:
                if field in book.keys():
                    item[field] = book.get(field)
            yield item
