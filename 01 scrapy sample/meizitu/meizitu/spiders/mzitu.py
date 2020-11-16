import scrapy
from ..items import ImagespiderItem


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['https://www.mzitu.com/']

    # allowed_domains = ['icanhazip.com']
    # start_urls = ['http://icanhazip.com/']
    #
    # def parse(self, response):
    #     print(response.text)

    def parse(self, response):
        modules = response.xpath('//ul[@id="menu-nav"]//a/@href').getall()
        for qwq in modules:
            yield scrapy.Request(qwq, self.parse_images)

    def images_download(self, response):
        item = ImagespiderItem()
        item['title'] = response.xpath('//h2[@class="main-title"]/text()').get()
        img_list = []
        img_start_url = response.xpath('//div[@class="main-image"]/p/a/img/@src').get()
        img_start_url = img_start_url[0: -6]
        img_nums = response.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()').get()
        for _ in range(1, int(img_nums) + 1):
            if _ < 10:
                img_list.append(img_start_url + '0' + str(_) + '.jpg')
            else:
                img_list.append(img_start_url + str(_) + '.jpg')

        # next_img = response.xpath('//div[@class="pagenavi"]/a[last()]/@href').get()
        item['imgurl'] = img_list
        yield item
        # yield scrapy.Request(next_img, self.images_download)

    def parse_images(self, response):
        articles = response.xpath('//ul[@id="pins"]//a/img/@alt').getall()
        article_links = response.xpath('//ul[@id="pins"]/li/a/@href').getall()
        # item = ArticleItem()
        for title, link in zip(articles, article_links):
            # item['title'] = title
            # item['link'] = link
            # yield item
            yield scrapy.Request(link, self.images_download)

        try:
            next_page = response.xpath('//div[@class="nav-links"]/a[last()]/@href').get()
            yield scrapy.Request(next_page, self.parse_images)
        except:
            print('当前为最后一页')
