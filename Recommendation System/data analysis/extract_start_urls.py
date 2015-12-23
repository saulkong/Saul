__author__ = 'xiaocong'

# -*- coding:utf-8 -*-


import codecs
import urllib2
import time
import json

raw_urls_file=codecs.open('/Users/xiaocong/Downloads/raw_urls_file.txt','r','utf-8')
raw_urls=[x for x in raw_urls_file.read().split('\n')]
start_urls_file=codecs.open('/Users/xiaocong/Downloads/start_urls_file.txt','a','utf-8')


for raw_url in raw_urls:
    request=urllib2.Request(raw_url)
    response=urllib2.urlopen(request)
    time.sleep(0.5)
    body=json.loads(response.read())
    for content in body['subjects']:
        url=content['url']
        print url
        start_urls_file.write(url+'\n')

start_urls_file.close()







