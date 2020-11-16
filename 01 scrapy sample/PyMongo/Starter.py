from pymongo import *

# 1、 连接数据库获取 Client对象
client = MongoClient('mongodb://182.92.193.59:27017')
# 2、 选择要连接数据库
db = client.py
# 3、 选择要连接的集合 若不存在则新建
stu = db.stu

# 4、 增加一条数据
s1 = {'name': '杨康', 'gender': True}
s1_id = stu.insert_one(s1).inserted_id

stu.insert_one(
    {'title': 'MongoDB 教程',
     'description': 'MongoDB 是一个 Nosql 数据库',
     'by': 'MongoDB中文网',
     'url': 'http://www.mongodb.org.cn',
     'tags': ['mongodb', 'database', 'NoSQL'],
     'likes': 100
     })
print(s1_id)
