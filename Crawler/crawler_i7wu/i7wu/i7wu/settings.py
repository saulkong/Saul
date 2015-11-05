# -*- coding: utf-8 -*-

# Scrapy settings for i7wu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import os

BOT_NAME = 'i7wu'

SPIDER_MODULES = ['i7wu.spiders']
NEWSPIDER_MODULE = 'i7wu.spiders'

PROJECT_DIR=os.path.abspath(os.path.dirname(__file__))

ITEM_PIPELINES={
    'i7wu.pipelines.cover_image.I7wuCoverImage':300,
    'i7wu.pipelines.bookfile.I7wuBookFile':300,
    'i7wu.pipelines.drop_none_download.DropEmptyBookFile':300,
    'i7wu.pipelines.mongodb.MongodbPipeline':300,
}

DOWNLOADER_MIDDLEWARES={'scrapy.downloadermiddleware.useragent.UserAgentMiddleware':None,
                       'i7wu.spiders.rotate_useragent.RotateUserAgentMiddleware':400}



FILE_STORE=os.path.join(PROJECT_DIR,'i7wumedia/files')
BOOK_FILE_STORE = os.path.join(PROJECT_DIR,'i7wumedia/book_files')
FILE_EXPIRES=30
BOOK_FILE_EXPIRES = 30

LOG_FILE='logs/scrapy.log'

MONGODB_SERVER='localhost'
MONGODB_PORT=27017
MONGODB_DB='i7wudb'


IMAGES_STORE=os.path.join(PROJECT_DIR,'i7wumedia/book_cover_image')
IMAGES_EXPIRES=30
IMAGES_THUMBS={
    'small':(50,50),
    'big':(270,270),
}

IMAGES_MIN_HEIGHT=0
IMAGES_MIN_WIDTH=0




BOOK_FILE_CONTENT_TYPE = ['application/file',
    'application/zip',
    'application/octet-stream',
    'application/x-zip-compressed',
    'application/x-octet-stream',
    'application/gzip',
    'application/pdf',
    'application/ogg',
    'application/vnd.oasis.opendocument.text',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/x-dvi',
    'application/x-rar-compressed',
    'application/x-tar',
    'multipart/x-zip',
    'application/x-zip',
    'application/x-winzip',
    'application/x-compress',
    'application/x-compressed',
    'application/x-gzip',
    'zz-application/zz-winassoc-arj',
    'application/x-stuffit',
    'application/arj',
    'application/x-arj',
    'multipart/x-tar',
    'text/plain',]

URL_GBK_DOMAIN = ['www.paofuu.com',
        'down.wmtxt.com',
        'www.txt163.com',
        'down.txt163.com',
        'down.sjtxt.com:8199',
        'file.txtbook.com.cn',
        'www.yyytxt.com',
        'www.27xs.org',
        'down.dusuu.com:8199',
        'down.txtqb.cn']

ATTACHMENT_FILENAME_UTF8_DOMAIN = []

FILE_EXTENTION = ['.doc','.txt','.docx','.rar','.zip','.pdf']

Drop_NoneBookFile = True


AUTOTHROTTLE_ENABLED=True
AUTOTHROTTLE_START_DELAY=3.0
AUTOTHROTTLE_CONCURRENCY_CHECK_PERIOD=10
AUTOTHROTTLE_MAX_DELAY=60

DOWNLOAD_DELAY=0.5

COOKIES_ENABLED=False

DEPTH_LIMIT=10

DOWNLOAD_TIMEOUT=500




# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'i7wu (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'i7wu.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'i7wu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'i7wu.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
