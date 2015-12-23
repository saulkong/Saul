# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field



class DoubanItem(Item):

    film_name=Field()
    film_director=Field()
    film_scriptwriter=Field()
    film_leading_role=Field()
    film_type=Field()
    film_screen_date=Field()
    film_runtime=Field()
    film_grading=Field()
    film_long_review=Field()
    film_brief_review=Field()
    film_description=Field()
    film_cover_url=Field()
    film_cover_path=Field()
    original_url=Field()
    enter_db_time=Field()
    mongodb_id=Field()
    film_id=Field()


