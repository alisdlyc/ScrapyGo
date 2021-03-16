# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

from itemadapter import ItemAdapter
import pymongo
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class MongoDBPipeline(object):

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
        # self.db[name].insert(dict(item))
        self.db['airbnbTest'].update({'user_id': item['user_id']}, {'$set': item}, True)
        return item

    def close_spider(self, spider):
        self.client.close()


class ImagesrenamePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['img_url']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield Request(image_url, meta={'name': item['user_id']})

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        # 提取url前面名称作为图片名。
        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        # filename = u'{0}/{1}.jpg'.format(name, name)
        filename = u'./{1}.jpg'.format(name, name)
        return filename
