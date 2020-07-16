import json
import logging

import scrapy
from jsonpath import jsonpath

from ..items import BookItem


class LibrarySpider(scrapy.Spider):
    name = 'library'
    allowed_domains = ['bupt.edu.cn', 'opac.bupt.edu.cn']
    start_urls = ['http://opac.bupt.edu.cn:8080/search-classify.html']

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'JSESSIONID=757EC0CC88EDACEE342BB6F5EE412B1E',
        'Referer': 'http://opac.bupt.edu.cn:8080/search-classify.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Host': 'opac.bupt.edu.cn:8080',
        'Origin': 'http://opac.bupt.edu.cn:8080'
    }

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

                    yield scrapy.FormRequest(
                        url='http://opac.bupt.edu.cn:8080//search-classify.json',
                        headers=self.headers,
                        formdata=dict(
                            # classnoAbs=item['classno'],
                            classnoAbs=third.xpath('./span[1]/text()').extract_first().replace(' ', ''),
                            pageNo='0',
                            pageSize='50',
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
        for _ in range(jsonpath(json.loads(response.text), '$..totalPage')[0]):
            yield scrapy.FormRequest(
                url='http://opac.bupt.edu.cn:8080//search-classify.json',
                headers=self.headers,
                formdata=dict(
                    # classnoAbs=item['classno'],
                    classnoAbs=Abs,
                    pageNo='%d' % _,
                    pageSize='50',
                    order='-1',
                ),
                callback=self.get_books_data,
                meta={'Abs': Abs,
                      'Heading': Heading}
            )

    def get_books_data(self, response):
        Abs = response.meta['Abs']
        Heading = response.meta['Heading']

        books = json.loads(response.text)['data']
        for book in books:
            item = BookItem()
            item['heading'] = Heading
            item['classno'] = Abs
            for field in item.fields:
                if field in book.keys():
                    item[field] = book.get(field)
            yield item