__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

from i7wu.pipelines.bookfile import NofilesDrop

class DropEmptyBookFile(object):

    Drop_EmptyBookFile=True

    @classmethod
    def from_crawler(cls,crawler):
        cls.Drop_EmptyBookFile=crawler.settings.get('Drop_EmptyBookFile',True)
        pipe=cls()
        pipe.crawler=crawler
        return pipe

    def process_item(self,item,spider):
        if not item.get('book_file_url',None):
            raise NofilesDrop(item['original_url'])

        return item
