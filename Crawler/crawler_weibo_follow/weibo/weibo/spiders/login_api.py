__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import os
import sys
import urllib
import urllib2
import cookielib
import base64
import re
import hashlib
import json
import rsa
import binascii



def get_su(user_name):
    username=urllib.quote(user_name)
    username=base64.encodestring(username)[:-1]
    return username

def get_sp_rsa(passwd,servertime,nonce):
    weibo_rsa_n=''
    message=str(servertime)+'\t'+str(nonce)+'\n'+passwd
    key=rsa.PublicKey(int(weibo_rsa_n,16),weibo_rsa_e)
    encropy_pwd=rsa.encrypt(message,key)
    return binascii.b2a_hex(encropy_pwd)


def get_prelogin_status(user_name):
    prelogin_url='http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su='\
                 +get_su(user_name)+'rsakt=mod&client=ssologin.js(v1.4.18)'
    data=urllib2.urlopen(prelogin_url).read()
    print 'Step1: Load prelogin url'
    p=re.compile('\((.*)\)')

    try:
        json_data=p.search(data).group(1)
        data=json.loads(json_data)
        servertime=str(data['servertime'])
        nonce=data['nonce']
        rsakv=data['rsakv']
        print 'Getting prelogin status succeed!!!!!'
        return servertime,nonce,rsakv
    except:
        print 'Getting prelogin status met error!!!!!'
        return None

def do_login(user_name,passwd,cookie_file):
    login_data={"entry":'weibo',
                "gateway":'1',
                "from":'',
                "savestate":'7',
                "useticket":'1',
                "pagerefer":'',
                'vsnf':'1',
                'su':'',
                "service":'miniblog',
                "servertime":'',
                "nonce":'',
                "pwencode":'rsa2',
                "rsakv":'',
                "sp":'',
                "encoding":'UTF-8',
                "url":'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
                "returntype":'META'

        }

    cookie_jar=cookielib.LWPCookieJar()
    cookie_support=urllib2.HTTPCookieProcessor(cookie_jar)
    opener2=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener2)
    login_url='http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'

    try:
        servertime,nonce,rsakv=get_prelogin_status(user_name)
    except:
        return

    login_data['su']=get_su(user_name)
    login_data['sp']=get_sp_rsa(passwd,servertime,nonce)
    login_data['servertime']=servertime
    login_data['nonce']=nonce
    login_data['rsakv']=rsakv
    login_data=urllib.urlencode(login_data)
    http_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1707.0 Safari/537.36',}

    req=urllib2.Request(login_url,data=login_data,headers=http_headers)
    response=urllib2.urlopen(req)
    text=response.read()
    print 'Step2: Signin with post_data'

    p=re.compile('location\.replace\(\'(.*?)\'\)')
    try:
        login_url2=p.search(text).group(1)
        data=urllib2.urlopen(login_url2).read()
        patt_feedback='feedBackUrlCallBack\((.*)\)'
        p=re.compile(patt_feedback,re.MULTILINE)
        feedback=p.search(data).group(1)
        feedback_json=json.loads(feedback)
        if feedback_json['result']:
            cookie_jar.save(cookie_file,ignore_discard=True,ignore_expires=True)
            print 'Step3: Save cookie after login succeeded'
            return 1
        else:
            return 0
    except:
        return 0

def get_login_cookie(url):
    from weibo.spiders import settings

    cookie_file=settings.COOKIE_FILE

    if not os.path.exists(cookie_file):
        user_name=settings.USER_NAME
        passwd=settings.PASSWORD
        do_login(user_name,passwd,cookie_file)

    try:
        cookie_jar=cookielib.LWPCookieJar(cookie_file)
        cookie_jar.load(ignore_discard=True,ignore_expires=True)
        print 'Load cookie succeeded1'
    except cookielib.LoadError:
        return None

    else:
        cookie_d={}
        #print cookie_jar
        for cookie in cookie_jar:
            domain=cookie.domain
            #print 'cookie infomation as followed:'+'\n'
            if url.find(domain)>0:
                cookie_d[cookie.name]=cookie.value

                #print cookie.name+'\t'+cookie.value

        return cookie_d


def load_cookie(cookie_file):
    try:
        cookie_jar=cookielib.LWPCookieJar(cookie_file)
        cookie_jar.load(ignore_discard=True,ignore_expires=True)
        cookie_support=urllib2.HTTPCookieProcessor(cookie_jar)
        opener=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        print 'Load cookie succeeded2'
        return 1
    except cookielib.LoadError:
        return 0

def login(user_name,passwd,cookie_file):
    if os.path.exists(cookie_file) and load_cookie(cookie_file):
        return True
    else:
        return do_login(user_name,passwd,cookie_file)


def test_with_mayun():
    test_url='http://weibo.com/mayun'
    response=urllib2.urlopen(test_url).read()
    p=re.compile(r'\$CONFIG\[\'uid\'\]')
    if not p.search(response):
        print 'Please Login'
    else:
        print 'Already Login'

if __name__=='__main__':
    from weibo.spiders import settings

    if os.path.exists(settings.COOKIE_FILE):
        print 'there is a cookie_file'

    test_with_mayun()

    if login(settings.USER_NAME,settings.PASSWORD,settings.COOKIE_FILE):
        print 'Login Weibo succeeded'
        test_with_mayun()
    else:
        print 'Login Weibo failed'









