__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

list_first_item=lambda x:x[0] if x else None

def list_item(item):
    if item:
         return [x for x in item.split('/').strip()]

