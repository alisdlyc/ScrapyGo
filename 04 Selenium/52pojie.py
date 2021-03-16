import selenium
from pymongo import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 1、 连接数据库获取 Client对象
client = MongoClient('mongodb://localhost:27017')
# 2、 选择要连接数据库
db = client.py
# 3、 选择要连接的集合 若不存在则新建
pojie = db.pojie

option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)

start_url = 'https://www.52pojie.cn/forum.php'
driver.get(start_url)
module_names = []
module_url = []
partition = []


def get_new(name, url):
    print(name)
    driver.get(url)
    articles = driver.find_elements_by_xpath('//tbody//th[@class="new"]/a[2]')

    for article in articles:
        print(article.text)
        print(article.get_attribute("href"))
        pojie.insert({'content': article.text, 'url': article.get_attribute("href")})


modules = driver.find_elements_by_xpath('//tbody/tr/td/h2/a')
for module in modules:
    module_names.append(module.text)
    module_url.append(module.get_attribute("href"))
    partition = zip(module_names, module_url)

for name, url in partition:
    get_new(name, url)
    print('--------------------------------------------')

