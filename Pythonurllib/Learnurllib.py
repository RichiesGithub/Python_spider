#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import urllib2
import urllib
import urlparse
import socket
import random
import cookielib

#通过GET 请求获取百度首页
# try:
#
#     response = urllib2.urlopen('http://www.baidu.com',timeout=0.1)
#     # response = urllib.urlopen('http://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except urllib2.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print 'TIME OUT!'

# #通过POST 请求获取
# value = {'word': 'hello'}
# data = urllib.urlencode(value)
# print data
# response = urllib2.urlopen('http://httpbin.org/post', data=data)
# print response.read()

#设置Header， Requesr 一共有三个参数， URL ， data，headers
#方法1
# url = 'http://httpbin.org/post'
# value = {'name':'Richie'}
# header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)','Host': 'httpbin.org'}
# data = urllib.urlencode(value)
# req = urllib2.Request(url,data,header)
# response = urllib2.urlopen(req)
# print response.read().decode('utf-8')
#
# print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

#方法2，这种好处是可以定义一个请求头的字典， 循环添加
url = 'http://httpbin.org/post'
value = {'name':'Richie'}
data = urllib.urlencode(value)
req = urllib2.Request(url,data)
ua_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
user_agent = random.choice(ua_list)
req.add_header('User-Agent',user_agent)
response = urllib2.urlopen(req)
print response.read().decode('utf-8')
print response.getcode()
print response.info()

#通过rulllib.request.ProxyHandler()可以设置代理,网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问,所以这个时候需要通过设置代理来爬取数据,没有翻墙工具， 没法实验
# proxy_handler = urllib2.ProxyHandler({
#     'https': 'https://14.118.135.10:8080',
#     'https': 'https://61.178.149.237:59042'
# })
# opener = urllib2.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())


#cookie中保存中我们常见的登录信息，有时候爬取网站需要携带cookie信息访问,这里用到了http.cookijar，用于获取cookie以及存储cookie











