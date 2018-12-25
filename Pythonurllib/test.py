#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

# _*_ coding:utf-8 _*_
import urllib2
import urllib
import cookielib
from lxml import etree

# #通过CookieJar()类构建一个cookieJar对象，用来保存cookie的值
# cookie = cookielib.CookieJar()
# #通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
# #参数就是构建的CookieJar()对象
# cookie_handler = urllib2.HTTPCookieProcessor(cookie)
# #构建一个自定义的opener
# opener = urllib2.build_opener(cookie_handler)
# # 通过自定义opener的addheaders的参数，可以添加HTTP报头参数
# opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')]
# #renren网的登录接口
# url = 'http://www.renren.com/PLogin.do'
# #需要登录的账号密码
# data = {'email':'13608311930','password':'lq910816'}
# # 通过urlencode()编码转换
# data = urllib.urlencode(data)
# # 第一次是POST请求，发送登录需要的参数，获取cookie
# request = urllib2.Request(url,data = data)
# response = opener.open(request)
# print response.read()

# def mainPageLoader():
#     url = 'https://tieba.baidu.com/f?kw=美女'
#
#     mainpageurl = url + '&pn=' + str(0)
#     print mainpageurl
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
#     req = urllib2.Request(mainpageurl, headers=headers)
#     response = urllib2.urlopen(req)
#     html = response.read()
#     content = etree.HTML(html)
#     contentlist = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
#     print contentlist
#
# if __name__ == '__main__':
#     mainPageLoader()

import urllib
import urllib2
from lxml import etree

def loadPage(url):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
    """
    request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    # 解析HTML文档为HTML DOM模型
    content = etree.HTML(html)
    # 返回所有匹配成功的列表集合
    link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        # 组合为每个帖子的链接
        #print link
        loadImage(fulllink)

# 取出每个帖子里的每个图片连接
def loadImage(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    request = urllib2.Request(link, headers = headers)
    html = urllib2.urlopen(request).read()
    # 解析
    content = etree.HTML(html)
    # 取出帖子里每层层主发送的图片连接集合
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    # 取出每个图片的连接
    for link in link_list:
        # print link
        writeImage(link)

def writeImage(link):
    """
        作用：将html内容写入到本地
        link：图片连接
    """
    #print "正在保存 " + filename
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # 文件写入
    request = urllib2.Request(link, headers = headers)
    # 图片原始数据
    image = urllib2.urlopen(request).read()
    # 取出连接后10位做为文件名
    filename = link[-10:]
    # 写入到本地磁盘文件内
    with open(filename, "wb") as f:
        f.write(image)
    print "已经成功下载 "+ filename

def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        #filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        #print fullurl
        loadPage(fullurl)
        #print html

        print "谢谢使用"

if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名:")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)