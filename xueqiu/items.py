# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XueqiuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    current = scrapy.Field()
    percent = scrapy.Field()
    change = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    high52w = scrapy.Field()
    low52w = scrapy.Field()
    marketcapital = scrapy.Field()
    amount = scrapy.Field()
    type = scrapy.Field()
    pettm = scrapy.Field()
    volume = scrapy.Field()
    hasexist = scrapy.Field()
