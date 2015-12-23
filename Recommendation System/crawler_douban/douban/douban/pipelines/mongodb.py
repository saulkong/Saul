__author__ = 'xiaocong'

# -*- coding:utf-8 -*-


import datetime
import traceback
import logging
from pymongo import MongoClient

class MongodbPipeline(object):
    MONGODB_SERVER='localhost'
    MONGODB_PORT=27017
    MONGODB_DB='doubandb'

    def __init__(self):

        try:
            client=MongoClient(self.MONGODB_SERVER,self.MONGODB_PORT)
            self.db=client[self.MONGODB_DB]
        except Exception as e:
            print ('ERROR(MongodbPipeline):%s'%(str(e),))
            traceback.print_exc()

    @classmethod
    def from_crawler(cls,crawler):
        cls.MONGODB_SERVER=crawler.settings.get('MONGODB_SERVER','localhost')
        cls.MONGODB_PORT=crawler.settings.getint('MONGODB_PORT',27017)
        cls.MONGODB_DB=crawler.settings.get('MONGODB_DB','doubandb')
        pipe=cls()
        pipe.crawler=crawler
        return pipe

    """
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
    """

    def process_item(self,item,spider):
        doubaninfo={
            'film_name':item.get('film_name'),
            'film_director':item.get('film_director',[]),
            'film_scriptwriter':item.get('film_scriptwriter',[]),
            'film_leading_role':item.get('film_leading_role',[]),
            'film_type':item.get('film_type',[]),
            'film_screen_date':item.get('film_screen_date',''),
            'fim_runtime':item.get('film_runtime',''),
            'film_grading':item.get('film_grading',[]),
            'film_long_review':item.get('film_long_review',''),
            'film_brief_review':item.get('film_brief_review',''),
            'film_description':item.get('film_description',''),
            'film_cover_url':item.get('film_cover_url',''),
            'film_cover_path':item.get('film_cover_path',''),
            'original_url':item.get('original_url',''),
            'film_id':item.get('film_id',''),
            'enter_db_time':datetime.datetime.utcnow(),
        }

        result=self.db['doubaninfo'].insert(doubaninfo)
        item['mongodb_id']=str(result)

        logging.log(logging.DEBUG,'Item %s write to MongoDB database %s doubaninfo'%(result,self.MONGODB_DB))
        return item