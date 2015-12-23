__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

from scrapy import Selector
from scrapy import Request
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from douban.items import DoubanItem
from douban.spiders.login_api import get_login_cookie
from douban.utils.select_result import list_first_item,list_item
import codecs

class DoubanSpider(Spider):




    name='douban'
    allow_domains=['douban.com']
    start_url__=codecs.open('/Users/xiaocong/Downloads/start_urls_deduplicated.txt','r','utf-8')
    start_url__=[x for x in start_url__.read().split('\n') if x]
    start_urls=start_url__

    def parse(self,response):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse_item)


    def parse_item(self, response):
        """
             film_name=Field()
             film_director=Field()
             film_scriptwriter=Field()
             film_leading_role=Field()
             film_type=Field()
             film_screen_date=Field()
             film_runtime=Field()
             film_grading=Field()
             film_long_review=Field()
             film_brief_review=Field()
             film_description=Field()
             film_cover_url=Field()
             film_cover_path=Field()
             original_url=Field()
             enter_db_time=Field()
             mongodb_id=Field()
             film_id=Field()
        """


        sel=Selector(response)
        item=DoubanItem()


        item['film_name']=sel.css('span[property="v:itemreviewed"]').xpath('text()').extract()[0]


        film_info=sel.css('#info')

        character_info=[x for x in film_info.css('.attrs')]

        director=[]
        director_info=character_info[0].css('a')
        for director_info_item in director_info:
            director_item=director_info_item.xpath('text()').extract()
            director.append(director_item[0])
        item['film_director']=director


        scriptwriter=[]
        scriptwriter_info=character_info[1].css('a')
        for scriptwriter_info_item in scriptwriter_info:
            scriptwriter_item=scriptwriter_info_item.xpath('text()').extract()
            scriptwriter.append(scriptwriter_item[0])
        item['film_scriptwriter']=scriptwriter

        leading_role=[]
        leading_role_info=character_info[2].css('a')
        for leading_role_info_item in leading_role_info:
            leading_role_item=leading_role_info_item.xpath('text()').extract()
            leading_role.append(leading_role_item[0])
        item['film_leading_role']=leading_role




        type=[]
        genre_info=film_info.css('span[property="v:genre"]')
        for genre_info_item in genre_info:
            type_item=genre_info_item.xpath('text()').extract()
            type.append(type_item[0])
        item['film_type']=type



        screen_date=[]
        screen_date_info=film_info.css('span[property="v:initialReleaseDate"]')
        for screen_date_info_item in screen_date_info:
            screen_date_item=screen_date_info_item.xpath('text()').extract()
            screen_date.append(screen_date_item[0])
        item['film_screen_date']=screen_date


        item['film_runtime']=film_info.css('span[property="v:runtime"]').xpath('text()').extract()[0][0:3]


        grading=[]
        grading_item={}
        grading_box=sel.css('.rating_wrap.clearbox')

        grading_item['num_of_people_to_grading']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract()[0]
        grading_item['average_grading']=grading_box.css('.rating_self.clearfix strong').xpath('text()').extract()[0]
        #print grading_item['average_grading']
        grading_item['stars5_grading']=grading_box.css('span:nth-of-type(2)::text').extract()[0]
        grading_item['stars4_grading']=grading_box.css('span:nth-of-type(4)::text').extract()[0]
        grading_item['stars3_grading']=grading_box.css('span:nth-of-type(6)::text').extract()[0]
        grading_item['stars2_grading']=grading_box.css('span:nth-of-type(8)::text').extract()[0]
        grading_item['stars1_grading']=grading_box.css('span:nth-of-type(10)::text').extract()[0]
        grading.append(grading_item)
        item['film_grading']=grading


        item['film_long_review']=sel.xpath('//*[@id="review_section"]/div[1]/h2/span/a/text()').extract()[0][2:]
        item['film_brief_review']=sel.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/text()').extract()[0].split(' ')[1]
        item['film_description']=sel.css('span[property="v:summary"]').xpath('text()').extract()[0].strip()
        item['film_cover_url']=sel.xpath('//*[@id="mainpic"]/a/img/@src').extract()[0]
        item['original_url']=response.url
        print response.url
        item['film_id']=response.url.replace('http://movie.douban.com/subject/','').replace('/','')

        return item





















