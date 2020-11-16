import scrapy
from music.items import MusicItem
# 01、 导入分布式爬虫类
from scrapy_redis.spiders import RedisSpider

# 02、 继承分布式爬虫类
class DiscogsRedisSpider(RedisSpider):
    name = 'discogs_redis'
    # 03、 注销start_urls和allowed_domains
    # allowed_domains = ['discogs.com']
    # start_urls = ['https://www.discogs.com/search/?sort=hot%2Cdesc&decade=2020&page=1']

    # 04、 设置redis-key, 用于存储start_url
    redis_key = 'music'

    # 05、 设置 __init__
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(DiscogsRedisSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        cards = response.xpath('//div[@id="search_results"]/div')
        next_page = 'https://www.discogs.com%s' % response.xpath('//a[@class="pagination_next"]/@href').get()
        for card in cards:
            # https://www.discogs.com/Joy-Division-Transmission/release/15622081
            url = 'https://www.discogs.com%s' % card.xpath('./a/@href').get()
            yield scrapy.Request(url, self.parse_info, dont_filter=True)
        yield scrapy.Request(next_page, self.parse, dont_filter=True)

    def parse_info(self, response):
        item = MusicItem()
        profile = response.xpath('//div[@class="profile"]')
        t1 = profile.xpath('./h1[@id="profile_title"]/span/span/a/text()').get().replace(' ', '').replace('\n', '').replace('\r', '')
        t2 = profile.xpath('./h1[@id="profile_title"]/span[2]/text()').get().replace(' ', '').replace('\n', '').replace('\r', '')
        item['Title'] = "%s-%s" % (t1, t2)
        content_list = profile.xpath('./div[@class="content"][1]//text()').getall()
        item['Label'] = "".join(content_list).replace(' ', '').replace('\n', '')

        Format = profile.xpath('./div[@class="content"][2]//text()').getall()
        item['Format'] = "".join(Format).replace(' ', '').replace('\n', '')

        Country = profile.xpath('./div[@class="content"][3]//text()').getall()
        item['Country'] = "".join(Country).replace(' ', '').replace('\n', '')

        Released = profile.xpath('./div[@class="content"][4]//text()').getall()
        item['Released'] = "".join(Released).replace(' ', '').replace('\n', '')

        Genre = profile.xpath('./div[@class="content"][5]//text()').getall()
        item['Genre'] = "".join(Genre).replace(' ', '').replace('\n', '')

        Style = profile.xpath('./div[@class="content"][6]//text()').getall()
        item['Style'] = "".join(Style).replace(' ', '').replace('\n', '')

        Credits = response.xpath('//div[@id="credits"]/div[1]/ul/li//text()').getall()
        item['Credits'] = "%".join(Credits).replace(' ', '').replace('\n', '')
        yield item





