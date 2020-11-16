import requests
import re
from lxml import etree

r = requests.get('https://bbs.machenike.com/forum.php?mod=viewthread&tid=22322&extra=&page=1')
print(r.text)
r = etree.HTML(r.text)

text = r.xpath('//div[@class="t_fsz"]//text()')
print(text)