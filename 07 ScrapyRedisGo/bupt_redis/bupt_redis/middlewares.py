# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from collections import defaultdict

import requests
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.exceptions import NotConfigured


class BuptRedisSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BuptRedisDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# class RandomProxyMiddleware(object):
#     url = 'http://icanhazip.com/'
#
#     def get_proxy(self):
#         return requests.get("http://182.92.193.59:5010/get/").json()
#
#     def delete_proxy(self, proxy):
#         requests.get("http://182.92.193.59:5010/delete/?proxy={}".format(proxy))
#
#     def get_local_ip(self):
#         return requests.get(self.url).text
#
#     def get_random_proxy(self):
#         local_ip = self.get_local_ip()
#
#         while True:
#             ip = self.get_proxy().get('proxy')
#             try:
#                 proxies = {"http": "http://" + ip, "https": "https://" + ip}
#                 html = requests.get(self.url, proxies=proxies)
#                 if not html.text == local_ip:
#                     return ip
#                 else:
#                     print(ip + '无效')
#                     self.delete_proxy(ip)
#             except Exception:
#                 self.delete_proxy(ip)
#
#     def __init__(self, settings):
#         # 2. 初始化配置及相关变量
#         self.stats = defaultdict(int)
#         self.max_failed = 3
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # 1. 创建中间件对象
#         if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
#             raise NotConfigured
#
#         return cls(crawler.settings)
#
#     def process_request(self, request, spider):
#         # 3. 为每个request对象分配一个随机的IP代理
#         if not request.meta.get('proxy'):
#
#             # TODO 从IP代理池中获取一个可用的IP
#             ip = self.get_random_proxy()
#             proxies = {"http": "http://" + ip, "https": "https://" + ip}
#             request.meta['proxy'] = proxies
#
#     def process_response(self, request, response, spider):
#         # 4. 请求成功则调用process_response
#         cur_proxy = request.meta.get('proxy')
#         # 判断是否被对方封禁
#         if response.status in (401, 403):
#             # 给相应的IP失败次数+1
#             self.stats[cur_proxy] += 1
#             print('%s got wrong code %s times' % (cur_proxy, self.stats[cur_proxy]))
#         # 当某个IP的失败次数累计到一定数量
#         if self.stats[cur_proxy] >= self.max_failed:
#             print('got wrong http code (%s) when use %s' \
#                   % (response.status, cur_proxy))
#             # 可以认为该IP被对方封禁了，从代理池中将该IP删除
#             self.remove_proxy(cur_proxy)
#             del request.meta['proxy']
#             # 将该请求重新安排调度下载
#             return request
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # 4. 请求失败则调用process_exception
#         cur_proxy = request.meta.get('proxy')
#         # 如果本次请求使用了代理，并且网络请求报错，认为该IP出现问题了
#         if cur_proxy and isinstance(exception, (ConnectionRefusedError, TimeoutError)):
#             print('error (%s) occur when use proxy %s' % (exception, cur_proxy))
#             self.remove_proxy(cur_proxy)
#             del request.meta['proxy']
#             return request
#
#     def remove_proxy(self, proxy):
#
#         # TODO 将失效的IP从代理池中移除
#         self.delete_proxy(proxy.get('http').replace('http://', ''))