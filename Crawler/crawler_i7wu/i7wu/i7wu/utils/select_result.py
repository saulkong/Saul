__author__ = 'xiaocong'

# -*- coding:utf-8 -*-


import types


NULL = [None,'null']

list_first_item = lambda x:x[0] if x else None

def strip_null(arg,null=None):

    if null is None:
        null = NULL

    if type(arg) is types.ListType:
        return [i for i in arg if i not in null]
    elif type(arg) is types.TupleType:
        return tuple([i for i in arg if i not in null])
    elif type(arg) is type(set()):
        return arg.difference(set(null))
    elif type(arg) is types.DictType:
        return {key:value for key,value in arg.items() if value not in null}

    return arg

def deduplication(arg):

    if type(arg) is types.ListType:
        return list(set(arg))
    elif type(arg) is types.TupleType:
        return tuple(set(arg))

    return arg

def link_strip(link):


    return link.strip("\t\r\n '\"")
