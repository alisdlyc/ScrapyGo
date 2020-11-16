import scrapy
from music.items import MusicItem
from scrapy_splash import SplashRequest

script = """
function main(splash, args)
  splash.images_enable = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  return {
    html = splash:html(),
  }
end
"""


class DiscogsSpider(scrapy.Spider):
    name = 'discogs'
    allowed_domains = ['discogs.com']
    start_urls = ['https://www.discogs.com/search/?sort=hot%2Cdesc&decade=2020&page=1']

    def parse(self, response):
        cards = response.xpath('//div[@id="search_results"]/div')
        next_page = 'https://www.discogs.com%s' % response.xpath('//*[@id="pjax_container"]/div[3]/form/div[1]/ul/li[2]/a/@href').get()
        for card in cards:
            # https://www.discogs.com/Joy-Division-Transmission/release/15622081
            url = 'https://www.discogs.com%s' % card.xpath('./a/@href').get()
            yield SplashRequest(url, self.parse_info, args={'lua_source': script, 'wait': 7})
        yield SplashRequest(next_page, self.parse, args={'lua_source': script, 'wait': 7})

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
