__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import os
import logging
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline
from i7wu.utils.select_result import list_first_item

class I7wuCoverImage(ImagesPipeline):
    """
    this is for download the book cover image and then complete the book_cover_image_path filed
    to the picture's path in the file system.
    """

    def __init__(self,store_uri,download_func=None):
        self.images_store=store_uri
        super(I7wuCoverImage,self).__init__(store_uri,download_func=None)

    def get_media_requests(self, item, info):
        if item.get('book_cover_image_url'):
            yield Request(item['book_cover_image_url'][0])

    def item_completed(self,results,item,info):
        if self.LOG_FAILED_RESULTS:
            msg='%s found errors processing %s'%(self.__class__.__name__,item)
            for ok,value in results:
                #print 'result: ',results
                if not ok:
                    logging.ERROR(value,msg,spider=info.spider)

        image_paths=[x['path'] for ok,x in results if ok]
        image_path=list_first_item(image_paths)
        item['book_cover_image_path']=os.path.join(os.path.abspath(self.images_store),image_path) if image_path else ""

        return item