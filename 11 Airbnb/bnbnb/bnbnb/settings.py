BOT_NAME = 'bnbnb'

SPIDER_MODULES = ['bnbnb.spiders']
NEWSPIDER_MODULE = 'bnbnb.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Cookie': "bev=1599227250_NTE3ODM0MjkyMzQw; frmfctr=wide; currency=CNY; cfrmfctr=DESKTOP; cbkp=4; flags=0; auth_jitney_session_id=bd850b2f-3129-4f20-9bf7-649f490c992e; _csrf_token=V4%24.airbnb.cn%24qRtuZ4hFZEg%24JPbyAnCa8Jy2VVfes-IvyL761H5c1DLAgxME1r60iNI%3D; _rmt=2--WzI3ODM3MTc0NCwiMzR8MXxreW04SmN5a200byt0Z2w0IiwiTTNYV2VEYkRQUUJ1Q3RqNEcwTDVTa0NlMEJHcXVoSi1XRnpNRFBxbHdTMCJd--a16b52158da414dd0d8e1e79477a85649f7c195d; li=1; _pt=1--WyIwMjMxYjcyNjNjNGE1MWY5MWI5NTJjMTA1YzkyNWU5Zjc4OTU4NjE2Il0%3D--80cdb402bf0603967304eda1c3c8c0eaa0d43dfc; _aat=0%7CFdR21GtdLclKrd9bzO2Uqzr4IkSdiN%2BuAPFnkBryXLP%2FJiIdxdUzQNK8jBCcfHzg; abb_fa2=%7B%22user_id%22%3A%2242%7C1%7CojqZinShg8WIN8mB4%2B2ZT8m86z093RJ0J%2BeOVHJ6NOwv1gNcIo7If98%3D%22%7D; rclu=%7B%22278371744%22%3D%3E%22QYPbvaD3XJGKmP8zLXdctUGlQWG9AFZ8IXC4u1Qdg40%3D%22%7D; rclmd=%7B%22278371744%22%3D%3E%22otp_phone%22%7D; roles=0; _airbed_session_id=ad0ace6ab898da701669eb7009900ad9; hli=1; cdn_exp_374ca02e6cda03955=control; _pykey_=f044ac26-601c-56bb-9462-02eae0723903; jitney_client_session_id=7cb2d6cb-f16f-4b2b-ac97-d90e2e08c174; jitney_client_session_created_at=1599269966; tzo=480; previousTab=%7B%22id%22%3A%225045bc49-7a50-48ac-beae-ffd7b96c0339%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.cn%2Frooms%2F%3Ftranslate_ugc%3Dfalse%26source_impression_id%3Dp3_1599273995_EnjRbsYQYF4ard4k%22%7D; __xsptplus840=840.2.1599273997.1599274169.2%234%7C%7C%7C%7C%7C%23%23%23; _user_attributes=%7B%22curr%22%3A%22CNY%22%2C%22guest_exchange%22%3A6.841749999999999%2C%22device_profiling_session_id%22%3A%221599227250--d456d11113cd142efb4aabb0%22%2C%22giftcard_profiling_session_id%22%3A%221599273800-278371744-f5dfac782cacdea16cbfd00e%22%2C%22reservation_profiling_session_id%22%3A%221599273800-278371744-91db036b54b05204dd698a51%22%2C%22id%22%3A278371744%2C%22hash_user_id%22%3A%220231b7263c4a51f91b952c105c925e9f78958616%22%2C%22eid%22%3A%22VhCbAE93E5Qx20uyNvgjJA%3D%3D%22%2C%22num_msg%22%3A0%2C%22num_notif%22%3A1%2C%22num_alert%22%3A1%2C%22num_h%22%3A0%2C%22num_trip_notif%22%3A0%2C%22name%22%3A%22%E4%BA%91%E8%B6%85%22%2C%22num_action%22%3A0%2C%22is_admin%22%3Afalse%2C%22can_access_photography%22%3Afalse%2C%22travel_credit_status%22%3Anull%2C%22referrals_info%22%3A%7B%22receiver_max_savings%22%3A%22%EF%BF%A5192%22%2C%22receiver_savings_percent%22%3A0%2C%22receiver_signup%22%3A%22%EF%BF%A50%22%2C%22referrer_guest%22%3A%22%EF%BF%A530%22%2C%22terms_and_conditions_link%22%3A%22%2Fhelp%2Farticle%2F2269%22%2C%22wechat_link%22%3A%22https%3A%2F%2Fwww.airbnb.cn%2Fc%2Fe761641%3Fcurrency%3DCNY%26s%3D11%22%2C%22offer_discount_type%22%3A%22tiered_savings%22%7D%7D; jitney_client_session_updated_at=1599274623",
    "referer": "https://www.airbnb.cn/users"  # 破解网站的防盗链
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'bnbnb.middlewares.BnbnbSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'bnbnb.middlewares.BnbnbDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'bnbnb.pipelines.MongoDBPipeline': 300,
    'bnbnb.pipelines.ImagesrenamePipeline': 300,
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
HTTPCACHE_ENABLED = False

MONGO_URL = '182.92.193.59'
MONGO_PORT = 27017
MONGO_DB = 'airbnb'

# 图片存储位置
IMAGES_STORE = './images'
