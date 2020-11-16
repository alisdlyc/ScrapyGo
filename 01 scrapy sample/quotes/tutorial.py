import scrapy
# scrapy runspider tutorial.py

class QuoteSpider(scrapy.Spider):
    name = 'quote',
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            # 返回括号里面的数据
            yield {
                'text': quote.xpath('./span/text()').extract_first(),
                'author': quote.xpath('./span/small/text()').extract_first()
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield response.follow(next_page, self.parse)
