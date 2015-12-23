__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import os
import urllib
import urllib2
import cookielib

def get_account(user_name):
    user_name=user_name
    return user_name

def get_password(user_passwd):
    user_passwd=user_passwd
    return user_passwd

def do_login(user_name,passwd,cookie_file):
    login_data={
        'source':'None',
        'redir':'http://www.douban.com',
        'form_email':'',
        'form_password':'',
    }
    cookie_jar=cookielib.LWPCookieJar()
    cookie_support=urllib2.HTTPCookieProcessor(cookie_jar)
    opener2=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener2)
    login_url='http://accounts.douban.com/login'
    login_data['form_email']=get_account(user_name)
    login_data['form_password']=get_password(passwd)
    http_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1707.0 Safari/537.36',}
    req=urllib2.Request(login_url,data=login_data,headers=http_headers)
    response=urllib2.urlopen(req)
    text=response.read()
    print 'Step1: Sign in with post_data'

    try:

        if cookie_jar:
            print cookie_jar
            cookie_jar.save(cookie_file,ignore_expires=True,ignore_discard=True)
            print 'Step2: Save cookies after login succeeded'
            return 1
        else:
            return 0
    except:
        return 0





def get_login_cookie(url):
    from douban.spiders import settings

    cookie_file=settings.COOKIE_FILE

    if not os.path.exists(cookie_file):
        user_name=settings.USER_NAME
        passwd=settings.PASSWORD
        do_login(user_name,passwd,cookie_file)

    try:
        cookie_jar=cookielib.LWPCookieJar(cookie_file)
        cookie_jar.load(ignore_discard=True,ignore_expires=True)
        print 'Load cookie succeeded'
    except cookielib.LoadError:
        return None
    else:
        cookie_d={}
        for cookie in cookie_jar:
            domain=cookie.domain
            if url.find(domain)>0:
                cookie_d[cookie.name]=cookie.value
        return cookie_d

