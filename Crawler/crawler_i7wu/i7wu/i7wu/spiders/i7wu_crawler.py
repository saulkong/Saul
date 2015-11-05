# -*-coding:utf-8 -*-


from scrapy import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.http import Request
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from i7wu.items import I7WuItem
from i7wu.utils.select_result import list_first_item,strip_null,deduplication
import logging

class I7WuSpider(CrawlSpider):
    name='i7wu'
    allow_domains=['i7wu.cn']
    start_urls=['http://www.i7wu.cn']
    rules=[Rule(sle(allow='/xiazai/txt/\d+.htm'),follow=True,callback='parse_item')]

    def parse_item(self,response):
        item=I7WuItem()
        sel=Selector(response)

        """
            mongodb_id=Field()
            book_name=Field()
            book_author=Field()
            book_description=Field()
            book_file_url=Field()
            book_file=Field()
            book_download=Field()
            book_cover_image_path=Field()
            book_cover_image_url=Field()
            original_url=Field()
        """
        item['book_name']=sel.xpath('//*[@id="txtleft"]/div[2]/h1/text()').extract()
        item['book_author']=sel.xpath('//*[@id="author"]/text()').extract()
        item['book_description']=sel.xpath('//*[@id="txtleft"]/div[2]/div[4]/p/text()').extract()
        item['book_cover_image_url']=sel.xpath('//*[@id="txtleft"]/div[1]/a/img/@src').extract()
        item['original_url']=response.url

        download=[]
        download_item={}
        download_item['url']=strip_null(deduplication([list_first_item(sel.xpath('//*[@id="txtdown"]/ul/li[1]/a/@href').extract()),
                                                       list_first_item(sel.xpath('//*[@id="txtdown"]/ul/li[2]/a/@href').extract())]))


        download_item['upload_time']=sel.xpath('//*[@id="txtleft"]/div[1]/ul[1]/li[5]/text()').extract()
        download_item['number_of_time_for_downloaded']=sel.xpath('//*[@id="txtleft"]/div[1]/ul[1]/li[4]/text()').extract()
        download_item['number_of_time_for_rating']=sel.xpath('//*[@id="rating_count_num"]/text()').extract()

        download.append(download_item)
        item['book_download']=download

        yield item

