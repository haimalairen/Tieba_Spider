# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import random
from fake_useragent import UserAgent
from manju_tools import RandomIPMiddleware

class IPMiddleware(RandomIPMiddleware):
    isPrint = False
    url='http://proxy.siyetian.com/apis_get.html?token=AesJWLNpWQ51kaFdXTENGMOpWS35kaJBTTEVEeNRUQ51STqFUeNpWR31ERjBTT6lkeOp2aw8EVNBTT6tmM.AM0ITNzITN2YTM&limit=1&type=0&time=0&split=0&split_text=&area=0&repeat=0&isp='
