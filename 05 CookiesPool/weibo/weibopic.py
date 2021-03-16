import json
import winreg

import requests
import re
import os
import time


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


# your spider code

def getHtml():
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while True:
        while retry_count > 0:
            try:
                requests.get('https://s.weibo.com', proxies={"http": "http://{}".format(proxy)})
                # 使用代理访问
                return proxy
            except Exception:
                print(proxy + '无效')
                retry_count -= 1
        # 删除代理池中代理
        delete_proxy(proxy)
        proxy = get_proxy().get("proxy")
        retry_count = 5


def getCookie():
    r = requests.get('http://localhost:5000/weibo/random')
    cookies = {}
    for line in r.text.split(','):
        name, value = line.strip().split(':', 1)
        cookies[name] = value
    return cookies

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4144.2 Safari/537.36'
}
number = 94

while True:
    print('抓取中......')  # 下面的链接填写微博搜索的链接
    url = f'https://s.weibo.com/weibo?q=%23%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F%23&wvr=6&b=1&Refer=SWeibo_box&page={number}'

    response = requests.get(url, cookies=getCookie(), proxies={"http": "http://{}".format(getHtml())})
    result = response.text
    detail = re.findall('data="uid=(.*?)&mid=(.*?)&pic_ids=(.*?)">', result)

    for part in detail:
        head = part[0]
        feet = part[2]
        feet = feet.split(',')
        for foot in feet:
            img_dir = os.path.join(os.curdir, head)
            if not os.path.exists(img_dir):
                os.mkdir(img_dir)
            else:
                continue
            url_x = f'https://wx1.sinaimg.cn/large/{foot}.jpg'  # 这里就是大图链接了
            response_photo = requests.get(url_x, headers=header)
            file_name = url_x[-10:]

            with open('./' + head + '/' + file_name, 'ab') as f:  # 保存文件
                f.write(response_photo.content)

    print('----------------------' + '第%d页获取完毕' % number + '----------------------')
    number += 1
    time.sleep(2)
