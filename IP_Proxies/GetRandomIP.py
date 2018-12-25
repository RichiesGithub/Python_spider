#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import requests
from fake_useragent import UserAgent
import MySQLdb

def getRandomIP():
    url = 'http://www.baidu.com'
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    IP = getIPFromDB()
    proxies = {IP[2].encode('utf-8').lower():IP[2].encode('utf-8').lower()+'://'+IP[0].encode('utf-8')+':'+IP[1].encode('utf-8')}
    print proxies
    try:
        response = requests.get(url,headers=headers,proxies = proxies,timeout = 10)
        if response.status_code == 200:
            print 'ok'
            return proxies
    except:
        getRandomIP()

def getIPFromDB():
    try:
        SQL = 'SELECT IP,PORT,TYPE FROM ip_proxies ORDER BY rand() limit 1'
        db = MySQLdb.connect("localhost", "root", "lq910816", "PythonDB", charset='utf8')
        cursor = db.cursor()
        cursor.execute(SQL)
        ip = cursor.fetchone()
        return ip
    except Exception,e:
        print e
    finally:
        cursor.close()

if __name__=='__main__':
    getRandomIP()



