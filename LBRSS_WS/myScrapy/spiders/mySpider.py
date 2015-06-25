# -*- coding: utf8 –*-
import scrapy
import json
from myScrapy.items import NewsItem

class MySpider(scrapy.Spider):
    name = "crawl_news"
    allowed_domains = ["youdao.com"]
    position = ['哈尔滨']#,'长春','沈阳','大连','呼和浩特','石家庄','青岛','开封','郑州','太原','拉萨','贵阳','长沙','合肥','南宁','海口','福州','广州','深圳','厦门','昆明','台北','杭州','宁波']

    def start_requests(self):
        BASE_URL = "http://news.youdao.com/search?q={}&start=0&ue=utf8&s=&tl=&keyfrom=news.index"
        # BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=true'
        for p in self.position:
            url = BASE_URL.format(p)
            yield scrapy.Request(url, self.parse)

    def parsePos(self, response):
        pos = json.loads(response.body)
        yield pos['results'][0]['geometry']['location']['lat']

    def parse(self, response):
        for sel in response.xpath('//li[@class="has-pic"]'):
            item = NewsItem()


            item['title'] = ''
            title_list = sel.xpath('h3/a/text()').extract()
            for i in range(len(title_list)):
                item['title'] += title_list[i]

            item['link'] = sel.xpath('h3/a/@href').extract()[0]

            item['desc'] = ''
            desc_list = sel.xpath('p/text()').extract()
            for i in range(len(desc_list)):
                item['desc'] += desc_list[i]

            yield item

