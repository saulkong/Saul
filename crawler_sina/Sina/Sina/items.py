# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class SinaItem(Item):
    publish_time=Field()
    title=Field()
    content=Field()
    base_url=Field()

