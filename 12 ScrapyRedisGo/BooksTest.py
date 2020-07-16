import json

import requests
from jsonpath import jsonpath

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=757EC0CC88EDACEE342BB6F5EE412B1E',
    'Referer': 'http://opac.bupt.edu.cn:8080/search-classify.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Host': 'opac.bupt.edu.cn:8080',
    'Origin': 'http://opac.bupt.edu.cn:8080'
}

for _ in ['A', 'B', 'C']:
    re = requests.post(
        url='http://opac.bupt.edu.cn:8080//search-classify.json',
        headers=headers,
        data=dict(
            # classnoAbs=item['classno'],
            classnoAbs=_,
            pageNo='1',
            pageSize='50',
            order='-1',
        ),
    )

    book_pages = jsonpath(json.loads(re.text), '$..totalPage')[0]
    total = jsonpath(json.loads(re.text), '$..total')[0]
    print('%s pages total is %s.....' % (book_pages, total))
