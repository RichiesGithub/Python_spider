#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import urllib2
import urllib
url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

# start和limit可以自己随便设置
formdata = {'start':'20','limit':'100'}

data = urllib.urlencode(formdata)
request = urllib2.Request(url,data = data,headers=headers)

response = urllib2.urlopen(request)
print response.read()