# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import datetime


class MongoPipeline(object):

    def __init__(self, mongourl, mongoport, mongodb):
        self.mongourl = mongourl
        self.mongoport = mongoport
        self.mongodb = mongodb

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongourl=crawler.settings.get("MONGO_URL"),
            mongoport=crawler.settings.get("MONGO_PORT"),
            mongodb=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongourl, self.mongoport)
        self.db = self.client[self.mongodb]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[str(datetime.date.today())].update({'timestamp': item['timestamp']}, {'$set': item}, True)
        # self.db[name].insert(dict(item))
        # self.db['discogs'].update({'url_token': item['url_token']}, {'$set': item}, True)
        return item

    def close_spider(self, spider):
        self.client.close()