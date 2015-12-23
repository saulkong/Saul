__author__ = 'xiaocong'

# -*- coding:utf-8 -*-



import logging
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self,user_agent=''):
        self.user_agent=user_agent

    def process_request(self,request,spider):
        ua=random.choice(self.user_agent_list)
        if ua:
            print '*************Current UserAgent:%s**************'%ua
            logging.log(logging.INFO,'Current UserAgent: '+ua)
            request.headers.setdefault('User-Agent',ua)

    user_agent_list=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
                     "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
                     "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
                     "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
                     "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
                     "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
                     "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                     "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
                     "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                     "Lenovo A376/S100 Release/11.2012 Mozilla/5.0 (Linux; U; Android 4.0.3) AppleWebKit/534.30"
                     "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET4.0C; .NET4.0E)",
                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                     "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
                     "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; InfoPath.2)",
                     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
                     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
                     "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
                     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) "
                     "Gecko/20100101 Firefox/6.0",
                     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2"
                     "Media Center PC 6.0; InfoPath.3; .NET4.0C; 2.X MetaSr 1.0)",
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1"
                     "(KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
                     "Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 "
                     "(KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
                     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
                     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
                     "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Coolpad 8297 Build/JDQ39) AppleWebKit/534.24 "
                     "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/4.9 (Baidu; P1 4.2.2)",
                     ]