#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import urllib2
from bs4 import BeautifulSoup
import re

# def mainPageLoader():
    # mainpageurl = 'https://tieba.baidu.com/f?kw=美女&pn=0'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    # req = urllib2.Request(mainpageurl, headers=headers)
    # response = urllib2.urlopen(req)
    # html = response.read()
    # # print html
    # print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    # soup = BeautifulSoup(html,'lxml')
    # # print soup
    # # print soup.find_all('a')
    # for x in soup.find_all(re.compile('<a\s.*?>.*?</a>')):
    #     print x
    # # print soup.name
    # # print soup.a.name
    # # print soup.a.attrs
    # # print soup.a['href']
    # # print soup.a.string
    # # print soup.head.contents
    # # print soup.head.children
    # # for child in soup.head.children:
    # #     print child
    # # for x in soup.find_all(re.compile('^a')):
    # #     print x
    # # print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    # # print soup
    # # print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    # # print soup.text
    # # for x in soup.find_all('a'):
    # #     print x
    #
    # # print soup.find('a').text
    # # print soup.find(id="frs_footer_tieba_report")
    # # print soup.prettify()

if __name__ == '__main__':
    mainPageLoader()