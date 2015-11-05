# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from twisted.enterprise import adbapi
from hashlib import md5
from MySQLdb import cursors
import MySQLdb
import logging
import pymongo


class SinaPipeline(object):

    def __init__(self):
        self.file=codecs.open('sina.json','wb',encoding='utf-8')




    def process_item(self, item, spider):
        line=json.dumps(dict(item)['base_url'])+'\n'
        self.file.write(line.decode('unicode_escape'))

        return item

    def spider_closed(self,spider):
        self.file.close()


class SinaMongoDBPipeline(object):
    pass

class SinaMySQLPipeline(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool

    @classmethod
    def from_settings(cls,settings):
        dbargs=dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool=adbapi.ConnectionPool('MySQLdb',**dbargs)
        return cls(dbpool)

    def process_item(self,item,spider):
        d=self.dbpool.runInteraction(self._do_upinsert,item,spider)
        """d.addErrback(self._handle_error,item,spider)"""

        return item

    def _do_upinsert(self,conn,item,spider):
        linkmd5id=self._get_linkmd5id(item)
        c=''.join(item['content'])
        item['content']=c



        conn.execute('select * from sinainfo where linkmd5id = %s',(linkmd5id,))
        ret=conn.fetchone()

        if ret:
            conn.execute('updata sinainfo set baseurl=%s,publishtime=%s,content=%s,title=%s where linkmd5id=%s',
                        (item['base_url'][:],item['publish_time'][0],item['content'][:],item['title'][0],linkmd5id))

        else:

            conn.execute("insert into sinainfo(baseurl,publishtime,content,title,linkmd5id) values(%s,%s,%s,%s,%s)",
                        (item['base_url'][:],item['publish_time'][0],item['content'][:],item['title'][0],linkmd5id))


    def _get_linkmd5id(selfself,item):
        return md5(item['base_url']).hexdigest()

    """def _handle_error(self,faulure,item,spider):
        logging.log(logging.ERROR,'failure')
        """






"""class SinaMySQLPipeline(object):
    def __init__(self):
        self.dbpool=adbapi.ConnectionPool('MySQLdb',
                                          db='Sinadb',
                                          user='root',
                                          passwd='180146906',
                                          cursorclass=MySQLdb.cursors.DictCursor,
                                          charset='utf8',
                                          use_unicode=True
                                          )
        self.ids_seen=set()


    def process_item(self,item,spider):
        query=self.dbpool.runInteraction(self._conditional_insert,item)
        return item

    def _conditional_insert(self,fx,item):


        linkmd5id=self._get_linkmd5id(item)
        if linkmd5id in self.ids_seen:
            tx.excute('updata sinainfo set baseurl=%s,publishtime=%s,content=%s,title=%s,linkmd5id=%s where linkmd5id=%s',
                        (item['base_url'],item['publish_time'],item['content'],item['title'],linkmd5id))
            pass

        else:
            self.ids_seen.add(linkmd5id)
            fx.execute("insert into sinainfo(baseurl,publishtime,content,title,linkmd5id) values(%s,%s,%s,%s,%s)",
                       (item['base_url'],item['publish_time'],item['content'],item['title'],linkmd5id))


    def _get_linkmd5id(self,item):
        return md5(item['base_url']).hexdigest()"""








