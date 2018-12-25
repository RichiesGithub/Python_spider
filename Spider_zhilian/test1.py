#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import urllib2
import urllib
from lxml import etree
from bs4 import BeautifulSoup
from lxml import etree
import requests



def get_one_html(url):
    headers = {

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",

        "Accept-Encoding": "gzip, deflate, sdch",

        "Accept-Language": "zh-CN,zh;q=0.8,mt;q=0.6",

        "Cache-Control": "max-age=0",

        "Connection": "keep-alive",

        "Host": "sou.zhaopin.com",

        "Referer": "http://www.zhaopin.com/",

        "Upgrade-Insecure-Requests": "1",

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"

    }
    html = requests.get(url,headers = headers).text
    print html

    soup = BeautifulSoup(html,"lxml")
    jobs = soup.select("#newlist_list_content_table > table")[1:]
    print jobs


if __name__ == '__main__':
    url = 'https://sou.zhaopin.com/?jl=489'
    get_one_html(url)
