#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
'''
运用XPATH 爬取美女吧帖子内的图片
'''
import urllib
import urllib2
from lxml import etree

class SpiderXPATH:

    def __init__(self):
        self.page=0
        self.Switch = True

    #定义一个主页面加载器，用于解析出每一个帖子的链接
    def mainPageLoader(self,url,page):
        mainpageurl = url+'&pn='+str(page)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        req = urllib2.Request(mainpageurl,headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()
        content = etree.HTML(html)
        link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        for link in link_list:
            imagepageurl = 'https://tieba.baidu.com/'+link
            self.imagePageLoder(imagepageurl)
    def imagePageLoder(self,url):
        headers = {'User-Agent': "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"}
        req = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()
        content = etree.HTML(html)
        contentlist = content.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
        for link in contentlist:
            self.saveImage(link)
        print'下载完成'
    def saveImage(self,link):
        headers = {'User-Agent': "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"}
        req = urllib2.Request(link, headers=headers)
        image = urllib2.urlopen(req).read()
        filename = link[-10]
        with open('C:\meinv\\'+filename,'wb') as f:
            f.write(image)


    def startWork(self,url):
        while self.Switch:
            print '开始第 '+ str(self.page/50+1)+' 页下载'
            self.mainPageLoader(url,self.page)
            command = raw_input('是否继续？继续请按空格，退出请输入quit:')
            if command == 'quit':
                self.Switch = False
            self.page+=50
        print 'thanks for used!'

if __name__ == '__main__':
    #主页面url：https://tieba.baidu.com/f?kw=美女=utf-8&pn=0
    url = 'https://tieba.baidu.com/f?'
    value = {'kw':'美女'}
    data = urllib.urlencode(value)
    mainpageurl = url+data
    spider = SpiderXPATH()
    spider.startWork(mainpageurl)



