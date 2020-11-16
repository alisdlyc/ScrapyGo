# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 存储数据的地方
import pymysql


class MysqlPipeline(object):
    # 在爬虫创建时执行
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='usrank',
            user='root',
            password='sd5.35365',
            charset='utf8',
        )
        self.cur = self.conn.cursor()

    # 在爬虫结束时执行
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    # 新增 item时执行
    def process_item(self, item, spider):
        # keys = item.keys()
        # values = [item[k] for k in keys]
        keys, values = zip(*item.items())
        sql = "insert into rank({}) values ({})".format(
            ','.join(keys),
            ','.join(['%s'] * len(values))
        )
        # self.cur.execute(sql, values)
        # self.conn.commit()
        return item

    # def process_item(self, item, spider):
    #     keys = item.keys()
    #     values =list(item.values())
    #     if None in values:
    #         values.remove(None)
    #     for val in values:
    #         str(val).replace(' ', '')
    #
    #     sql = "insert into rank({}) values ({}})".format(
    #         ','.join(keys),
    #         ','.join(['%s'] * len(values))
    #     )
    #     print(sql)
    #     print(self.cur.execute(sql, values))
    #     self.conn.commit()
    #     return item