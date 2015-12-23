__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import codecs

start_urls_file=codecs.open('/Users/xiaocong/Downloads/start_urls_file.txt','r','utf-8')

url=[x for x in start_urls_file.read().split('\n')]
url=set(url)
url=list(url)
start_urls_deduplicated_file=codecs.open('/Users/xiaocong/Downloads/start_urls_deduplicated.txt','a','utf-8')
for u in url:
    start_urls_deduplicated_file.write(u+'\n')
    print u

start_urls_file.close()
start_urls_deduplicated_file.close()
