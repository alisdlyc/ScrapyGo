# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class ArticleItem(scrapy.Item):
#     # define the fields for your item here like:
#     title = scrapy.Field()
#     link = scrapy.Field()


class ImagespiderItem(scrapy.Item):
    title = scrapy.Field()
    imgurl = scrapy.Field()
