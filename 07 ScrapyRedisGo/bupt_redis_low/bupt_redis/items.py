# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    heading = scrapy.Field()
    classno = scrapy.Field()

    recCtrlId = scrapy.Field()
    classnoNo = scrapy.Field()
    classnoAbs = scrapy.Field()
    title = scrapy.Field()
    authors = scrapy.Field()
    isn = scrapy.Field()
    publisher = scrapy.Field()
    pubdateDate = scrapy.Field()
    libraryId = scrapy.Field()
    reGrade = scrapy.Field()
    commentCount = scrapy.Field()
    libraryName = scrapy.Field()
    guancangCount = scrapy.Field()
    kejieCount = scrapy.Field()
    imgUrl = scrapy.Field()