__author__ = 'xiaocong'

import re
import json

from scrapy.selector import HtmlXPathSelector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from Sina.items import SinaItem
import logging

class SinaSpider(CrawlSpider):
    name='sina'
    allowed_domains=['sina.com.cn']
    start_urls=['http://finance.sina.com.cn']
    rules=[Rule(sle(allow='http://finance.sina.com.cn/\w+/\w+/\d{,8}/\d{,13}.shtml'),follow=True,callback='parse_item')]

    def parse_item(self,response):
        item=SinaItem()
        sel=HtmlXPathSelector(response)
        base_url=get_base_url(response)

        item['title']=sel.select('//h1[@id="artibodyTitle"]/text()').extract()
        item['publish_time']=sel.select('//div[@id="wrapOuter"]/div/div[4]/span/text()').extract()
        item['content']=sel.select('//div[@id="artibody"]/p/text()').extract()
        item['base_url']=base_url
        yield item

    def _process_request(self,request):
        logging.log(logging.INFO,'process'+str(request))
        return request




