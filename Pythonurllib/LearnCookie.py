#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import cookielib
import urllib2
import urllib

#模拟登陆人人网学习Cookie

#创建Cookie
cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_handler)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')]
# value = {"loginName":'13608311930','password':'lq910816'}
# data = urllib.urlencode(value)
# request = urllib2.Request('https://passport.zhaopin.com/login',data=data)
request = urllib2.Request('https://passport.zhaopin.com/login')
response = opener.open(request)
print response.read()

#获取到cookie后， 我们就可以爬取其他页面了
# request_other = opener.open('http://app.renren.com/?origin=54171')
# print request_other.read()

