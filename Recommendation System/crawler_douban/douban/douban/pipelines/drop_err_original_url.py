__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

from douban.pipelines.url import UrlDrop

class DropErrUrl(object):
    """
    Drop film_name is empty
    """
    Drop_NoneName=True

    @classmethod
    def from_crawler(cls,crawler):
        cls.Drop_NoneName=crawler.settings.get('Drop_NoneName',True)
        pipe=cls()
        pipe.crawler=crawler
        return pipe

    def process_item(self,item,spider):
        if not item.get('film_name',None):
            raise UrlDrop(item['original_url'])

        return item

