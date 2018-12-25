#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import requests


# kw = {'wd':'python'}
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
#
# # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
# response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)
#
# # 查看响应内容，response.text 返回的是Unicode格式的数据
# print response.text
#
# # 查看响应内容，response.content返回的字节流数据
# print response.content
#
# # 查看完整url地址
# print response.url
#
# # # 查看响应头部字符编码
# print response.encoding
#
# # 查看响应码
# print response.status_code
#
# print response.cookies

#Session

#创建session对象， 可以保存cookie值
ssion = requests.session()
# 2. 处理 headers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
# 3. 需要登录的用户名和密码
data = {"email":"13608311930", "password":"lq910816"}
# 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
ssion.post("http://www.renren.com/PLogin.do",data=data,headers=headers)
response = ssion.get("http://zhibo.renren.com/news/108")
print response.text




