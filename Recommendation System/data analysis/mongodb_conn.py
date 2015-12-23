__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

from pymongo import MongoClient
import traceback

class Mongodb_connect(object):
    MONGODB_SERVER='localhost'
    MONGODB_PORT=27017
    MONGODB_DB='doubandb'

    def __init__(self):

        try:
            client=MongoClient(self.MONGODB_SERVER,self.MONGODB_PORT)
            self.db=client[self.MONGODB_DB]
        except Exception as e:
            print ("ERROR(Mongodb):%s "%(str(e),))
            traceback.print_exc()

    def conn(self):
        return self.db
