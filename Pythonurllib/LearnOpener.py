#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import urllib
import urllib2
#自定义简单的opener

#1 构建一个handler ， 处理HTTP 请求,可以添加debugLevel
handler = urllib2.HTTPHandler(debuglevel=1)
#2 创建一个opener,参数是handler
opener = urllib2.build_opener(handler)
request = urllib2.Request('http://www.baidu.com/s')
#3 调用自定义的opener方法， 发送http请求
response = opener.open(request)
print response.read()

