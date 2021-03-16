import requests
import random
from time import sleep
from lxml import etree
from pymongo import *

url = 'https://www.discogs.com/search/'
# 连接MongoDB数据库
client = MongoClient('mongodb://35.220.172.244:27000')
db = client.formusic
stu = db.music
# 爬取的页面
page_num = 1

user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
]


def get_music_url(url, page_num):
    body = {
        'sort': 'hot%2Cdesc',
        'decade': 2020,
        'page': page_num,
    }
    # 更改User-Agent
    random_user_agent = random.choice(user_agent_list)
    header = {
        'User-Agent': random_user_agent,
    }
    r = requests.get(url, headers=header, data=body, timeout=60)
    res = etree.HTML(r.text)
    cards = res.xpath('//div[@id="search_results"]/div')
    for card in cards:
        url = 'https://www.discogs.com%s' % card.xpath('./a/@href')[0]
        uid = card.xpath('./@data-object-id')[0]
        stu.insert({
            'url': url,
            'uid': uid})

    page_num += 1
    print('--------第%d页, %d---------' % (page_num, r.status_code))


# 总page数为 11w/50
while page_num < 2379:
    get_music_url(url, page_num)
    sleep(3)
    page_num += 1
