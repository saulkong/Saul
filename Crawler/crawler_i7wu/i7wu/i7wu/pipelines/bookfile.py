__author__ = 'xiaocong'

# -*- coding:utf-8 -*-


import os
import itertools
import logging
from scrapy.item import Item
from scrapy.http import Request
from scrapy.utils.misc import arg_to_iter
from twisted.internet.defer import Deferred,DeferredList
from i7wu.utils.select_result import list_first_item
from i7wu.pipelines.file import FilePipeline,FSFilesStore,FileException
from scrapy.exceptions import DropItem,NotConfigured

class NofilesDrop(DropItem):
    """ Product with no files exception"""

    def __init__(self,original_url='',*args):
        self.original_url=original_url
        DropItem.__init__(self,*args)


    def __str__(self):
        print "DROP(NofilesDrop):"+self.original_url
        return DropItem.__str__(self)

class BookFileException(FileException):
    """ General book file error exception """

class FSBookFilesStore(FSFilesStore):
    pass

class I7wuBookFile(FilePipeline):
    """
        This is for download the book file and then define the book_file field
        to the file's path in the file system
    """

    MEDIA_NAME='bookfile'
    EXPIRES=90
    BOOK_FILE_CONTENT_TYPE=[]
    URL_GBK_DOMAIN=[]
    ATTACHMENT_FILENAME_UTF8_DOMAIN=[]
    STORE_SCHEMES={
        '':FSBookFilesStore,
        'file':FSBookFilesStore,
    }

    FILE_EXTENTION=['.doc','.txt','.docs','.rar','.zip','.pdf']

    def __init__(self,store_uri,download_func=None):
        super(I7wuBookFile,self).__init__(store_uri=store_uri,download_func=download_func)
        if not store_uri:
            raise NotConfigured
        self.bookfile_store=store_uri
        self.store=self._get_store(store_uri)
        self.item_download={}

    @classmethod
    def from_settings(cls,settings):
        cls.EXPIRES = settings.getint('BOOK_FILE_EXPIRES', 90)
        cls.BOOK_FILE_CONTENT_TYPE = settings.get('BOOK_FILE_CONTENT_TYPE',[])
        cls.ATTACHMENT_FILENAME_UTF8_DOMAIN = settings.get('ATTACHMENT_FILENAME_UTF8_DOMAIN',[])
        cls.URL_GBK_DOMAIN = settings.get('URL_GBK_DOMAIN',[])
        cls.FILE_EXTENTION = settings.get('FILE_EXTENTION',[])
        store_uri = settings['BOOK_FILE_STORE']
        return cls(store_uri)

    def process_item(self,item,spider):
        """
        custom process_item func,so it will manage the Request result.
        """

        info=self.spiderinfo[spider]
        requests=arg_to_iter(self.get_media_requests(item,info))
        dlist=[self._process_request(r,info) for r in requests]
        dfd=DeferredList(dlist,consumeErrors=True)
        dfd.addCallback(self.item_completed,item,info)
        return dfd.addCallback(self.another_process_item,item,info)

    def another_process_item(self,result,item,info):
        """
        custom process_item func,so it will manage the Request result.
        """

        assert isinstance(result,(Item,Request)),"I7wuBookFile pipeline item_completed must return Item or Request,got %s" %\
                                                 (type(result))

        if isinstance(result,Item):
            return result
        elif isinstance(result,Request):
            dlist=[self._process_request(r,info) for r in arg_to_iter(result)]
            dfd=DeferredList(dlist,consumeErrors=True)
            dfd.addCallback(self.item_completed,item,info)
            return dfd.addCallback(self.another_process_item,item,info)
        else:
            raise NofilesDrop

    def get_media_requests(self, item, info):
        """
            Only download once per book,so it pick out one from all of the download urls.
        """

        if item.get('book_download'):
            downloadfile_urls = [i['url'] for i in item.get('book_download') if i['url']]
            downloadfile_urls = list(set(itertools.chain(*downloadfile_urls)))
            first_download_file = list_first_item(downloadfile_urls)
            self.item_download[item['original_url']] = downloadfile_urls[1:]
            if first_download_file:
                return Request(first_download_file)

    def item_completed(self, results, item, info):
        if self.LOG_FAILED_RESULTS:
            msg = '%s found errors proessing %s' % (self.__class__.__name__, item)
            for ok, value in results:
                if not ok:
                    logging.ERROR(value, msg, spider=info.spider)

        bookfile_paths_urls = [(x['path'],x['url']) for ok, x in results if ok]
        bookfile_path_url = list_first_item(bookfile_paths_urls)
        if bookfile_path_url:
            item['book_file'] = os.path.join(os.path.abspath(self.bookfile_store),bookfile_path_url[0])
            item['book_file_url'] = bookfile_path_url[1]
            return item
        else:
            if self.item_download[item['original_url']]:
                next = list_first_item(self.item_download[item['original_url']])
                self.item_download[item['original_url']] = self.item_download[item['original_url']][1:]
                return Request(next)
            else:
                return item

    def is_valid_content_type(self,response):
        """
            judge whether is it a valid response by the Content-Type.
        """
        content_type = response.headers.get('Content-Type','')

        return content_type not in self.BOOK_FILE_CONTENT_TYPE






