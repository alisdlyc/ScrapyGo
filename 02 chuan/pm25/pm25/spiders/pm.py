import scrapy


class PmSpider(scrapy.Spider):
    name = 'pm'
    allowed_domains = ['86pm25.com']
    start_urls = ['http://m.86pm25.com/city/beijing.html']

    def parse(self, response):
        area = response.xpath('/html/body/div[1]/ul[1]/li/div[1]//text()').getall()
        pm = response.xpath('/html/body/div[1]/ul[1]/li/div[4]//text()').getall()
        datetime = response.xpath('/html/body/div[1]/div[2]/div[3]/font/text()').getall()
        date = str(datetime).split('更新：')[1].split('\'')[0]
        for a, p in zip(area, pm):
            print(date + str(a) + ',' + str(p).replace('μg/m³', ''))


