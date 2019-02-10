# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitchtrendItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TwitchChennelsInfoItem(scrapy.Item):
    date = scrapy.Field()
    time = scrapy.Field()
    rank = scrapy.Field()
    games = scrapy.Field()
    channels = scrapy.Field()
    viewers = scrapy.Field()
