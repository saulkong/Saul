__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import os
import logging
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline
from douban.utils.select_result import list_first_item

class FilmCoverImage(ImagesPipeline):
    """
    this is for download the film image and generate film_cover_path
    """

    def __init__(self,store_uri,download_func=None):
        self.image_store=store_uri
        super(FilmCoverImage,self).__init__(store_uri,download_func=None)

    def get_media_requests(self, item, info):
        if item.get('film_cover_url'):
            yield Request(item['film_cover_url'])

    def item_completed(self, results, item, info):
        if self.LOG_FAILED_RESULTS:
            msg='%s found errors processing %s'%(self.__class__.__name__,item)
            for ok,value in results:
                if not ok:
                    logging.error(msg,value,spider=info.spider)

        image_paths=[value['path'] for ok,value in results if ok]
        image_path=list_first_item(image_paths)
        item['film_cover_path']=os.path.join(os.path.abspath(self.image_store),image_path) if image_path else ''

        return item