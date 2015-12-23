__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import types
from pymongo import MongoClient
from pymongo import ASCENDING,DESCENDING

DATABASE_NAME='doubandb'
DATABASE_HOST='localhost'
DATABASE_PORT=27017
client=None
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

INDEX={
    'doubaninfo':
        {
            (('film_name',ASCENDING),('film_director',ASCENDING)):{'name':'film_name_director'},
            (('film_director',ASCENDING),('film_id',ASCENDING)):{'name':'film_director_id'},
            'film_name':{'name':'film_name'},
            'film_director':{'name':'film_director'},
            'film_id':{'name':'film_id','unique':True},
        }
}

#def drop_database(database_name,client):
#    if database_name and client:
#        client.drop_database(database_name)

def create_index(client):
    for k,v in INDEX.items():
        for key,kwargs in v.items():
            client[DATABASE_NAME][k].ensure_index(list(key) if type(key)==types.TupleType else key)

if __name__=='__main__':
    client=MongoClient(DATABASE_HOST,DATABASE_PORT)
    #drop_database(DATABASE_NAME,client)
    create_index(client)

