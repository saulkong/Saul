# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item,Field


class I7WuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mongodb_id=Field()
    book_name=Field()
    book_author=Field()
    book_description=Field()
    book_file_url=Field()
    book_file=Field()
    book_download=Field()
    book_cover_image_path=Field()
    book_cover_image_url=Field()
    original_url=Field()

