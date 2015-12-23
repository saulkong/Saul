__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import os
from scrapy.exceptions import DropItem


class UrlException(Exception):
    """Original url err exception"""

    def __init__(self,url=None,*args):
        self.url=url
        Exception.__init__(self,*args)

    def __str__(self):
        print ('Error(original url Exception):%s'%(Exception.__str__(self),))
        return Exception.__str__(self)

class UrlDrop(DropItem):
    """
    Drop wrong original url
    """
    def __init__(self,original_url='',*args):
        self.original_url=original_url
        DropItem.__init__(self,*args)

        def __str__(self):
            print ('DROP(URLDROP):'+self.original_url)
            return DropItem.__str__(self)