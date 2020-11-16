# -*- coding: utf-8 -*-

# Scrapy settings for qianmu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qianmu'

SPIDER_MODULES = ['qianmu.spiders']
NEWSPIDER_MODULE = 'qianmu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qianmu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
DOWNLOAD_TIMEOUT = 10
PROXIES = [
    'http://61.135.185.118:80',
    'http://112.80.255.77:80',
    'http://117.185.16.253:80',
    'http://163.125.250.148:8088',
    'http://180.97.104.97:80',
    'http://211.137.52.158:8080',
    'http://163.177.151.76:80',
    'http://117.185.17.144:80',
    'http://123.125.115.192:80',
    'http://163.177.151.76:80',
    'http://123.125.115.74:80',
    'http://112.80.255.29:80',
    'http://101.4.136.34:81',
    'http://183.232.232.69:80',
    'http://61.135.185.160:80',
    'http://180.149.144.223:80',
    'http://180.149.145.160:80',
    'http://61.135.185.153:80',
    'http://119.190.199.32:8060',
    'http://123.125.115.215:80',
    'http://180.149.145.139:80',
    'http://112.80.248.18:80',
    'http://61.135.185.103:80',
    'http://61.135.185.118:80',
    'http://117.185.17.177:80',
    'http://117.185.17.177:80',
    'http://182.61.62.23:80',
    'http://61.135.185.160:80',
    'http://61.135.185.78:80',
    'http://112.253.11.113:8000',
    'http://112.247.168.64:8060',
    'http://180.149.144.224:80',
    'http://123.125.114.21:80',
    'http://183.232.231.239:80',
    'http://61.135.185.118:80',
    'http://123.125.115.219:80',
    'http://111.206.37.244:80',
    'http://163.177.151.76:80',
    'http://222.74.202.227:9999',
    'http://61.135.185.78:80',
    'http://61.135.185.160:80',
    'http://61.135.185.90:80',
    'http://111.206.37.248:80',
    'http://183.232.231.133:80',
    'http://112.80.255.29:80',
    'http://183.232.231.133:80',
    'http://221.180.170.104:8080',
    'http://112.247.168.64:8060',
    'http://112.80.255.77:80',
    'http://117.185.17.16:80',
    'http://112.247.168.64:8060',
    'http://61.135.185.69:80',
    'http://183.232.232.69:80',
    'http://61.135.169.121:80',
    'http://119.52.0.242:80',
    'http://123.125.115.249:80',
    'http://117.185.16.31:80',
    'http://117.185.16.31:80',
    'http://1.160.95.237:8080',
    'http://61.135.169.121:80',
    'http://222.74.202.227:9999',
    'http://182.61.62.74:80',
    'http://119.52.0.242:80',
    'http://117.185.17.17:80',
    'http://111.206.37.248:80',
    'http://202.108.23.174:80',
    'http://180.97.104.97:80',
    'http://122.234.169.44:8060',
    'http://222.74.202.228:9999',
    'http://180.97.33.212:80',
    'http://180.97.104.170:80',
    'http://123.125.115.183:80',
    'http://61.135.185.68:80',
    'http://61.135.186.222:80',
    'http://180.97.34.35:80',
    'http://112.80.248.18:80',
    'http://180.97.33.66:80',
    'http://163.177.151.224:80',
    'http://61.135.185.152:80',
    'http://180.97.33.212:80',
    'http://111.206.37.248:80',
    'http://61.135.185.112:80',
    'http://211.137.52.159:8080',
    'http://180.149.145.160:80',
    'http://111.206.37.68:80',
    'http://180.97.33.78:80',
    'http://123.125.115.74:80',
    'http://112.80.248.18:80',
    'http://221.180.170.104:8080',
    'http://111.206.37.100:80',
    'http://111.206.37.248:80',
    'http://61.135.186.243:80',
    'http://202.101.135.18:8888',
    'http://61.135.185.68:80',
    'http://223.241.2.57:4216',
    'http://123.125.115.192:80',
    'http://61.135.186.80:80',
    'http://123.125.115.215:80',
    'http://61.135.185.103:80',

]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2
# 使用自定义的插件
MYEXT_ENABLED = True
MYEXT_ITEMCOUNT = 5
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qianmu.middlewares.QianmuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'qianmu.middlewares.RandomProxyMiddleware': 749,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   # 'scrapy.extensions.telnet.TelnetConsole': None,
    'qianmu.extensions.SpiderOpenCloseLogging': 1,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'qianmu.pipelines.MysqlPipeline': 301,
   # 'qianmu.pipelines.RedisPipeline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 启用HTTP请求缓存，下次再遇到该url时不再需要请求远程网站
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
