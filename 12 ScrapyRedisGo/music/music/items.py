# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Label = scrapy.Field()
    Format = scrapy.Field()
    Country = scrapy.Field()
    Released = scrapy.Field()
    Genre = scrapy.Field()
    Style = scrapy.Field()
    Credits = scrapy.Field()
