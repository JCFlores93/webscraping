# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Spider
from scrapy.loader import ItemLoader 

class QuotesSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    h1_tag = scrapy.Field()
    tag = scrapy.Field()
    pass
