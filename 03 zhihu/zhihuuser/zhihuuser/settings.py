# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_TIMEOUT = 10
PROXIES = [
    'http://210.59.0.156:80',
    'http://117.180.227.81:80',
    'http://61.135.185.38:80',
    'http://61.135.185.78:80',
    'http://116.62.140.86:8080',
    'http://61.227.74.178:80',
    'http://222.74.202.227:9999',
    'http://221.182.31.54:8080',
    'http://220.181.111.37:80',
    'http://111.206.37.68:80',
    'http://121.40.124.218:80',
    'http://117.185.17.144:80',
    'http://47.75.161.251:80',
    'http://61.135.185.92:80',
    'http://221.122.91.59:80',
    'http://218.66.253.145:80',
    'http://111.206.37.244:80',
    'http://180.149.144.223:80',
    'http://61.135.185.160:80',
    'http://180.97.33.94:80',
    'http://61.135.186.222:80',
    'http://115.223.7.110:80',
    'http://101.231.104.82:80',
    'http://111.206.37.161:80',
    'http://54.223.115.227:80',
    'http://47.112.142.82:80',
    'http://61.135.169.121:80',
    'http://202.108.22.5:80',
    'http://117.131.119.116:80',
    'http://183.232.231.133:80',
    'http://222.74.202.228:9999',
    'http://61.135.185.103:80',
    'http://61.135.185.20:80',
    'http://61.135.185.90:80',
    'http://117.180.227.100:80',
    'http://217.61.127.253:80',
    'http://222.73.144.63:80',
    'http://124.11.184.111:80',
    'http://203.204.200.103:80',
    'http://61.135.185.112:80',
    'http://218.59.139.238:80',
    'http://150.138.106.155:80',
    'http://149.248.56.105:80',
    'http://61.135.185.118:80',
    'http://47.96.7.111:80',
    'http://118.190.199.163:80',
    'http://182.61.62.23:80',
    'http://117.180.227.11:80',
    'http://112.80.40.76:80',
    'http://220.181.77.210:80',
    'http://183.236.52.212:80',
    'http://182.61.62.74:80',
    'http://61.135.186.80:80',
    'http://113.161.68.30:80',
    'http://47.104.15.198:80',
    'http://111.206.37.100:80',
    'http://47.114.117.238:80',
    'http://61.135.185.156:80',
    'http://112.80.255.29:80',
    'http://175.17.208.2:80',
    'http://159.138.3.119:80',
    'http://61.135.185.152:80',
    'http://117.185.16.226:80',
    'http://61.135.185.68:80',
    'http://221.122.91.66:80',
    'http://111.206.37.248:80',
    'http://129.226.184.8:80',
    'http://117.185.17.17:80',
    'http://111.13.100.91:80',
    'http://39.106.223.134:80',
    'http://103.235.46.154:80',
    'http://117.185.16.31:80',
    'http://180.97.33.78:80',
    'http://45.221.83.192:80',
    'http://61.135.186.243:80',
    'http://221.122.91.65:80',
    'http://183.232.231.76:80',
    'http://221.180.170.104:8080',
    'http://218.25.39.34:80',
    'http://211.144.213.145:80',
    'http://218.66.253.144:80',
    'http://47.114.142.53:80',
    'http://61.135.185.172:80',
    'http://47.102.194.42:8080',
    'http://119.23.207.56:80',
    'http://36.232.236.4:80',
    'http://180.97.33.249:80',
    'http://61.135.185.176:80',
    'http://58.61.154.153:8080',
    'http://61.135.185.12:80',
    'http://61.135.185.31:80',
    'http://117.180.227.80:80',
    'http://112.80.255.77:80',
    'http://39.96.84.127:80',
    'http://180.97.33.144:80',
    'http://218.60.8.99:3129',
    'http://60.205.132.71:80',
    'http://163.204.240.83:9999',
    'http://117.185.17.151:80',
    'http://47.106.162.218:80',
    'http://183.232.231.239:80',
    'http://39.137.69.7:80',
    'http://61.135.185.153:80',
    'http://39.137.69.10:80',
    'http://103.140.79.242:8080',
    'http://123.56.161.63:80',
    'http://61.135.185.111:80',
    'http://202.108.23.174:80',
    'http://211.137.52.158:8080',
    'http://117.185.17.145:80',
    'http://180.97.33.93:80',
    'http://117.180.227.78:80',
    'http://61.135.185.69:80',
]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Cookie': '_zap=74f8b653-778a-461e-a4b1-1ccef083b587; _xsrf=d9389f48-d18c-4d6a-86fc-530213cb7c17; d_c0="AFDSSgk3WhGPTs7neTp7CPw-rDFedffI9wQ=|1590892001"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1590892002; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1590891775,1590892002; _ga=GA1.2.978309757.1590892003; l_n_c=1; n_c=1; q_c1=4139418f9bd24e2aa9c3125bb76c82b9|1591334389000|1591334389000; tst=r; SESSIONID=FtNG2iAGZ7NLC5lSWDL9TRVGfMdWXWUlDAgl1sAaPTs; JOID=V1ATAEgk47Tx6GPGdCK46TfRR0Rmb5n_ttwHiTZ42fS4q1CnKX7JsqjjYM1x5EBK-UTLo_4PdXLpsG6nYiybNIk=; osd=WlkVB0kp6rL26W7PciW55D7XQEVrZp_4t9EOjzF51P2-rFGqIHjOs6XqZspw6UlM_kXGqvgIdH_gtmmmbyWdM4g=; capsion_ticket="2|1:0|10:1594041850|14:capsion_ticket|44:NjI0NjQxYzJmNjhhNGY0ODllZDczZTNhMWQ0MWEwZTk=|2d8b516bd7675d4b3f39272308de6409503eebe5f4daf53618154a2a2a5e6f25"; z_c0="2|1:0|10:1594041873|4:z_c0|92:Mi4xSFFPS0NnQUFBQUFBVU5KS0NUZGFFU1lBQUFCZ0FsVk5FWFR3WHdCaEcwUnFsaVpSZDRNSE85RVZYeHFBY2dYak1B|a5133c1b11c3d02a10a08584fd682465b20d572c2cdbc182b75c7424dbffb5c9"; unlock_ticket="AADnDjsFzQ0mAAAAYAJVTRktA1_AWplLkNkDhh_1sPAgMhftx7o0CA=="; KLBRSID=e42bab774ac0012482937540873c03cf|1594042689|1594040630'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'zhihuuser.middlewares.RandomProxyMiddleWare': 749,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuuser.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MONGO_URL = 'localhost'
MONGO_DATABASE = 'zhihu'
