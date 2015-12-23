__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import urllib2
import codecs
import time


seed=[
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%88%B1%E6%83%85&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8F%AF%E6%92%AD%E6%94%BE&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E5%86%B7%E9%97%A8%E4%BD%B3%E7%89%87&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8D%8E%E8%AF%AD&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E6%AC%A7%E7%BE%8E&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E9%9F%A9%E5%9B%BD&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E6%97%A5%E6%9C%AC&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8A%A8%E4%BD%9C&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E5%96%9C%E5%89%A7&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%88%B1%E6%83%85&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E6%82%AC%E7%96%91&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E6%81%90%E6%80%96&sort=recommend&page_limit=20&page_start=',
'http://movie.douban.com/j/search_subjects?type=movie&tag=%E6%96%87%E8%89%BA&sort=recommend&page_limit=20&page_start=',
]

joint_number=[]
for i in range(0,1000,20):
    joint_number.append(str(i))

template_for_drop_url='{"subjects":[]}'
raw_urls=[]
raw_urls_file=codecs.open('/Users/xiaocong/Downloads/raw_urls_file.txt','a','utf-8')
for i in range(len(seed)):
    for j in joint_number:
        time.sleep(0.5)
        url=seed[i]+j
        request=urllib2.Request(url)
        time.sleep(1)
        response=urllib2.urlopen(request)
        if response.read().strip()==template_for_drop_url:
            break
        else:
            raw_urls.append(url)
            print url
            raw_urls_file.write(url+'\n')

raw_urls_file.close()




