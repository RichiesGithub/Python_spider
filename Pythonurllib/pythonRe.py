#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import re

# pattern = re.compile('\d')    #将正则表达式编译成一个pattern规则对象
#
# pattern.match()    #从起始位置开始往后查找，返回第一个符合规则的，只匹配一次
# pattern.search()   #从任意位置开始往后查找，返回第一个符合规则的，只匹配一次
# pattern.findall()  #所有的全部匹配，返回列表
# pattern.finditer() #所有的全部匹配，返回的是一个迭代器
# pattern.split()    #分割字符串，返回列表
# pattern.sub()      #替换
#
# re.I   #表示忽略大小写
#
# re.S   #表示全文匹配

pattern = re.compile(r"\d+")
str ='aaa123bbb456'
m = pattern.match(str)
n = pattern.findall(str)
l = pattern.split(str)
print n
print l