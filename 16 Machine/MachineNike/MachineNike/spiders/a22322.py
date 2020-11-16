# -*- coding: utf-8 -*-
import scrapy
import re


class A22322Spider(scrapy.Spider):
    name = '22322'
    allowed_domains = ['machenike.com']
    start_urls = ['https://bbs.machenike.com/forum.php?mod=viewthread&tid=22322&extra=&page=1']
    a0 = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0

    # https://bbs.machenike.com/forum.php?mod=viewthread&tid=22322&extra=&page=1
    def parse(self, response):
        text = response.xpath('//div[@class="t_fsz"]//text()').getall()
        next_page = 'https://bbs.machenike.com/%s' % response.xpath(
            '//div[@class="pgs mtm mbm cl"]//div[@class="pg"]/a[last()]/@href').get()
        self.a0 += len(re.findall(r'.*?(申请试用)(Machcreator创物者CK7键盘|.*?CK7|.*?创物者键盘|.*?ck7|.*?键盘)', ''.join(text)))
        self.a1 += len(re.findall(r'.*?(申请试用)(Machcreator创物者CK1无线键鼠套餐|.*?无线键鼠套餐|.*?键鼠套餐|.*?CK1|.*?ck1|.*?键鼠套装)', ''.join(text)))
        self.a2 += len(re.findall(r'.*?(申请试用)(M8魔鬼鱼鼠标|.*?鼠标|.*?M8|.*?m8)', ''.join(text)))
        self.a3 += len(re.findall(r'.*?(申请试用)(机械师迷你护颈仪|.*?护颈仪)', ''.join(text)))
        self.a4 += len(re.findall(r'.*?(申请试用)(机械师智能按摩贴|.*?按摩贴)', ''.join(text)))
        yield scrapy.Request(next_page, self.parse)
        print('当前CK7键盘共%d人' % self.a0)
        print('当前CK1无线键鼠套餐共%d人' % self.a1)
        print('当前M8魔鬼鱼鼠标共%d人' % self.a2)
        print('当前机械师迷你护颈仪共%d人' % self.a3)
        print('当前机械师智能按摩贴共%d人' % self.a4)
        print('-------------------')
        print('')
