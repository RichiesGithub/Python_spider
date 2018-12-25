#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
# 爬取内涵段子

import urllib2
import re

class duanziSpider:
    def __init__(self):
        self.page = 1
        self.Switch = True

    #页面加载器
    def loadPage(self,page):
        print '开始第 '+str(page)+' 页数据爬取'
        if page == 1:
            url = 'https://www.neihan8.com/article/index.html'
        else:
            url = 'https://www.neihan8.com/article/index_'+str(page)+'.html'
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        req = urllib2.Request(url,headers=headers)
        respon = urllib2.urlopen(req)
        html = respon.read()
        #清洗数据
        patterncontent = re.compile(r'<div\sclass="desc">(.*?)</div>',re.S)
        patterntitle = re.compile(r'<h3><a\s.*?class="title".*?>(.*?)</a></h3>',re.S)
        content = patterncontent.findall(html)
        del(content[0])
        title = patterntitle.findall(html)
        contents = dict(zip(title,content))
        self.dealPage(contents,page)
    #文件写入
    def writetofile(self,items):
        with open('C:\duanzi.txt','a') as f:
            f.write(items)
    #处理单页数据
    def dealPage(self,contents,page):
        print '正在写入第 ' + str(page) + ' 页数据'
        for title,content in contents.items():
            self.writetofile(title+'\n')
            self.writetofile(content+'\n')
            self.writetofile('\n')
        print '第 '+str(page)+' 页数据写入完成'
    #调度器
    def startWork(self):
        while self.Switch:
            self.loadPage(self.page)
            command = raw_input("如果继续爬取，请按回车（退出输入quit)")
            if command == 'quit':
                self.Switch=False
            self.page+=1
        print 'Thanks for used'

if __name__ == '__main__':
    spider = duanziSpider()
    spider.startWork()





















