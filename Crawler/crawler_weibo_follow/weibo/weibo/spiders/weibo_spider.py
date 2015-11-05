__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

from scrapy import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.http import Request
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from weibo.items import WeiboItem
from weibo.spiders.login_api import get_login_cookie
import time
import re
import os
import urllib
import urllib2
import hashlib
import base64
import rsa
import binascii
import json


class WeiboSpider(CrawlSpider):
    name='weibo'

    allowed_domains=['weibo.com']
    start_urls=['http://www.weibo.com']
    rules=[Rule(sle(allow=r'^http:\/\/(www\.)?weibo.com/[a-z]/.*'),follow=True,callback='parse_item',process_request='process_request'),]
    cookies=None

    def process_request(self,request):
       request=request.replace(**{'cookies':self.cookies})
       return request





    def start_requests(self):

        for url in self.start_urls:
            if not self.cookies:
                self.cookies=get_login_cookie(url)
                #print self.cookies
            return [Request(url,dont_filter=True,cookies=self.cookies,meta={'cookiejar':1})]

    def extract_weibo_response(self,response):
        script_set=response.xpath('//script')
        script=''
        for s in script_set:

            try:
                s_text=s.xpath('text()').extract()[0]


            except:
                return response
            if s_text.find('WB_feed_detail')>-1:
                script=s_text
                #print script
                break

        kw={'body':script}
        response=response.replace(**kw)
        return response

    def _parse_response(self,response,callback,cb_kwargs,follow=True):
        response=self.extract_weibo_response(response)
        filename=response.url.split('/')[-2]+'.htm'
        with open(filename,'wb') as f:
            f.write(response.body)
        return super(WeiboSpider,self)._parse_response(response,callback,cb_kwargs,follow)

    def parse_item(self,response):
        sel=Selector(response)

        msg_nodes=sel.xpath('//*[@class="WB_feed WB_feed_profile"][2]/div')


        items=[]
        if msg_nodes:
            for msg in msg_nodes:
                item=WeiboItem()
                try:
                    c=msg.xpath('.//div[@class="WB_detail"]/div/text()').extract()[0]
                    content=c.encode('utf-8')
                except Exception,e:
                    pass
                else:
                    item['content']=content
                    item['url']=response.url
                    items.append(item)
        return items











