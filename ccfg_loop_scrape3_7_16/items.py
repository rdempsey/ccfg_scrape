# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CcfgLoopScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    h4_header = scrapy.Field()
    paragraph_text = scrapy.Field()
    url = scrapy.Field()
