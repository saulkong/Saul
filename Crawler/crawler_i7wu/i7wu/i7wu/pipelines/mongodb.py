# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import traceback
import logging
from pymongo import MongoClient


class I7WuPipeline(object):
    def process_item(self, item, spider):
        return item

class MongodbPipeline(object):

    MONGODB_SERVER='localhost'
    MONGODB_PORT=27017
    MONGODB_DB='i7wudb'

    def __init__(self):
        try:
            client=MongoClient(self.MONGODB_SERVER,self.MONGODB_PORT)
            self.db=client[self.MONGODB_DB]
        except Exception , e:
            traceback.print_exc()


    @classmethod
    def from_crawler(cls,crawler):
        cls.MONGODB_SERVER=crawler.settings.get('MONGODB_SERVER','localhost')
        cls.MONGODB_PORT=crawler.settings.get('MONGODB_PORT',27017)
        cls.MONGODB_DB=crawler.settings.get('MONGODB_DB','i7wudb')
        pipe=cls()
        pipe.crawler=crawler
        return pipe

    def process_item(self,item,spider):

        """
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

        """


        i7wuinfo={
            'book_name':item.get('book_name',''),
            'book_author':item.get('Field',[]),
            'book_desciption':item.get('book_description',''),
            'book_file_url':item.get('book_file_url',''),
            'book_file':item.get('book_file',''),
            'book_download':item.get('book_download',[]),
            'book_cover_image_path':item.get('book_cover_image_path',''),
            'book_cover_image_url':item.get('book_file_url',''),
            'original_url':item.get('original_url','')

        }

        result=self.db['i7wuinfo'].insert(i7wuinfo)
        item['mongodb_id']=str(result)

        logging.log(logging.DEBUG,"item %s wrote to MongoDB database %s  i7wuinfo"%(result,self.MONGODB_DB))
        return item



