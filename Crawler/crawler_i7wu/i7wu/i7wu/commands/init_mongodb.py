__author__ = 'xiaocong'

# -*- coding:utf-8 -*-



import types
from pymongo import ASCENDING,DESCENDING
from pymongo import MongoClient

"""
    book_name=Field()
    book_author=Field()
    book_description=Field()
    book_cover_image_path=Field()
    book_download_site=Field()
    book_file_url=Field()
    book_file=Field()
    book_upload_time=Field()
    book_total_download=Field()

"""


DATABASE_NAME='i7wudb'
client=None
DATABASE_HOST='localhost'
DATABASE_PORT=27017
INDEX={'i7wuinfo':
           {
               (('book_name','ASCENDING'),('author','ASCENDING')):{'name':'book_name_author','unique':'True'},
               'book_name':{'name':'book_name'},
               'author':{'name':'author'},

           }
}


def drop_database(database_name):
    if database_name and client:
        client.drop_database(database_name)

def create_index():

    for k,v in INDEX.items():
        for key,kwargs in v.items():
            client[DATABASE_NAME][k].ensure_index(list(key) if type(key)==types.TupleType else key,**kwargs)

if __name__=='__main__':
    client=MongoClient(DATABASE_HOST,DATABASE_PORT)
    drop_database(DATABASE_NAME)
    create_index()














