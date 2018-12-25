#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import requests
import re
from lxml import etree

def spider(url):
    headers = {
            'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.5,zh-HK;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Cookie': 'urlfrom2=121126445; adfbid2=0;…3d7240-1327104-167a10d62c7211',
            'Host': 'jobs.zhaopin.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64;x64;rv:63.0) Gecko/20100101 Firefox/63.0'
        }
    html = requests.get(url,headers=headers).text
    print html

    content = etree.HTML(html)
    neednumber = content.xpath("//div[@class='info-three l']/span[4]")[0].text.encode('utf-8')
    joblocal = content.xpath("//div[@class='info-three l']/span[1]/a")[0].text.encode('utf-8')
    joblight = re.search(r'.*JobWelfareTab = \'(.*?)\'',html).group(1).encode('utf-8')
    jobdesc = str(content.xpath("//div[@class='responsibility pos-common']/div[@class='pos-ul']")[0].xpath('string(.)').encode('utf-8'))





if __name__=="__main__":
    URL = 'https://jobs.zhaopin.com/CC676235428J00092991109.htm'
    spider(URL)