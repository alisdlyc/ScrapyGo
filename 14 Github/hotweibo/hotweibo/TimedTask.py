import os
import time
from scrapy import cmdline


def hot():
    os.system('scrapy crawl hot')


while True:
    hot()
    time.sleep(60)
