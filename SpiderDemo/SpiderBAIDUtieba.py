#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import urllib2
import urllib

#load page
def loadpage(url,filename):
    print '正在下载' + filename
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    req = urllib2.Request(url,headers=headers)
    content = urllib2.urlopen(req).read()
    return content

def writehtml(html,filename):
    print '正在写入'+filename
    with open(unicode('C:\Users\qli25\PycharmProjects\\testfile'+filename,'utf-8'),'w') as f:
        f.write(html)
    print '_'*30



#贴吧爬虫调度器，负责组合处理每个页面的url
def tiebaSpider(halfurl,startpage,endpage):
    for page in range(startpage,endpage+1):
        pn = urllib.urlencode({'pn':page})
        filename = '第' + str(page) + '页.html'
        fullurl = halfurl+'&'+ str(pn)
        html = loadpage(fullurl,filename)
        writehtml(html,filename)

if __name__ =='__main__':
    kw = raw_input("name: ")
    startpage = int(raw_input('startpae:'))
    endpage = int(raw_input('endpage: '))
    halfurl = 'http://tieba.baidu.com/f?'
    key = urllib.urlencode({'kw':kw})
    halfurl = halfurl+key
    tiebaSpider(halfurl,startpage,endpage)



