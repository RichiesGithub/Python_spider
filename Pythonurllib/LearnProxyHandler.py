#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import urllib2
#会封IP ， 使用自定义代理

handler =urllib2.ProxyHandler({'http':'136.228.128.6:36826'})
# handler =urllib2.ProxyHandler()
opener = urllib2.build_opener(handler)
requers = urllib2.Request('http://www.baidu.com/s')
# 如果想能够全局应用opener的话， 如下，
#urllib2.install_opener(opener)#这样urlopen（）也可以使用自定义代理
resopnse = opener.open(requers)

print resopnse.read()



