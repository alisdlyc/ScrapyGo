# -*- coding: utf-8 -*-

# Scrapy settings for weibosearch project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibosearch'

SPIDER_MODULES = ['weibosearch.spiders']
NEWSPIDER_MODULE = 'weibosearch.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'weibosearch (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COOKIE = '_T_WM=98313187201; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqQcoGAh_A54RcmyuaJ.sB5JpX5KzhUgL.FoqNeKqESK-EeKz2dJLoIpqLxKBLBo.L1-BLxK.LB.zL12-feo2E; SUB=_2A25yJXw8DeRhGeNI7FAU8ijPyjqIHXVR5gR0rDV6PUJbkdAKLU6nkW1NSCwQbzQ8_YyDuoHciRLaFLEzvLHppBio; SUHB=0Jvg96NrgYhnEo; SCF=AozIbjx45h0r5XZ5R0iWDZOjD5RmXFWU6UNZjMFqyO-Xw88dtc5tfsw1e2QvgatlWNWaSxWNob4wvQevMmQe4vA.; SSOLoginState=1596001388'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'cookie': ' _T_WM=98313187201; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqQcoGAh_A54RcmyuaJ.sB5JpX5KzhUgL.FoqNeKqESK-EeKz2dJLoIpqLxKBLBo.L1-BLxK.LB.zL12-feo2E; SUB=_2A25yJXw8DeRhGeNI7FAU8ijPyjqIHXVR5gR0rDV6PUJbkdAKLU6nkW1NSCwQbzQ8_YyDuoHciRLaFLEzvLHppBio; SUHB=0Jvg96NrgYhnEo; SCF=AozIbjx45h0r5XZ5R0iWDZOjD5RmXFWU6UNZjMFqyO-Xw88dtc5tfsw1e2QvgatlWNWaSxWNob4wvQevMmQe4vA.; SSOLoginState=1596001388',
    'user-agent': ' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

COOKIES_POOL_URL = 'http://localhost:5000/weibo/random'

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'weibosearch.middlewares.WeibosearchSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'weibosearch.middlewares.CookiesMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'weibosearch.pipelines.WeibosearchPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
