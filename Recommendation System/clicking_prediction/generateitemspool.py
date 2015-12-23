__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import codecs

def GenerateItemsPool(train_set):

    items_pool=codecs.open('/Users/xiaocong/Downloads/moviedata/items_pool.txt','a','utf-8')
    train_set=[x for x in train_set.read().split('\n') if x]
    for train_set_item in train_set:
        user,item,rating,time=train_set_item.split('::')
        items_pool.write(item+'\n')
    items_pool.close()

if __name__=='__main__':
    readfile=codecs.open('/Users/xiaocong/Downloads/moviedata/train_set.txt','r','utf-8')

    GenerateItemsPool(readfile)
    readfile.close()
