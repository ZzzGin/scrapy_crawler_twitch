# -*- coding: utf-8 -*-
import scrapy
from twitchTrend.items import TwitchChennelsInfoItem
import datetime

class TwitchdbSpider(scrapy.Spider):
    name = 'twitchdb'
    allowed_domains = ['www.twitchdb.info/top-games']
    start_urls = ['http://www.twitchdb.info/top-games']

    def parse(self, response):
        # self.log("I just visited: " + response.url)
        twitchInfoItem = TwitchChennelsInfoItem()
        twitchInfoItem['rank'] = response.css("td:nth-child(1)::text").extract()
        twitchInfoItem['games'] = response.css("b::text").extract()
        twitchInfoItem['channels'] = response.css("td:nth-child(4)::text").extract()
        twitchInfoItem['viewers'] = response.css("td:nth-child(5)::text").extract()
        twitchInfoItem['date'] = datetime.date.today()
        twitchInfoItem['time'] = datetime.datetime.time(datetime.datetime.now())
        yield twitchInfoItem