import os
import sys

import requests

if __name__ == '__main__':
    keyword = '北方栖姬'
    if len(sys.argv) > 1:
        keyword = sys.argv[1]

    url = 'https://www.52doutu.cn/api/'
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
    }
    offset = 1
    LIMIT = 60
    # 构造请求体
    # 网站为动态的js请求，且每次只能爬取60页
    body = {
        'types': 'search',
        'action': 'searchpic',
        'wd': keyword,
        'limit': LIMIT,
        'offset': offset
    }

    image_lists = []
    count = 0

    # 若当前目录下 images文件夹不存在则创建+

    
    image_dir = os.path.join(os.curdir, keyword)
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    while offset <= LIMIT:

        # 解析json响应中图片的下载地址
        r = requests.post(url, headers=header, data=body).json()
        rows = r['rows']
        for row in rows:
            print('append: ' + row['url'])
            image_lists.append(row['url'])

        # 下载图片并存入文件中
        for img_url in image_lists:
            try:
                img_res = requests.get(img_url)
                with open('./%s/%d.jpg' % (keyword, count), 'wb') as f:
                    count += 1
                    for chunk in img_res.iter_content(1024):
                        f.write(chunk)
            except Exception:
                print(Exception)
            image_lists.remove(img_url)

            offset += 1

    print('爬取结束，共下载%s张表情包' % count)