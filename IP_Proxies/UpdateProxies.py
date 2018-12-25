#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import requests
import MySQLdb
from fake_useragent import UserAgent

def removeUselessIP():
    url = 'http://www.baidu.com'
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    IPs = getIPFromDB()
    for IP in IPs:
        try:
            proxies = {IP[2].encode('utf-8').lower(): IP[2].encode('utf-8').lower() + '://' + IP[0].encode('utf-8') + ':' + IP[1].encode('utf-8')}
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200:
                continue
        except:
            try:
                SQL = 'DELETE FROM ip_proxies WHERE IP='+'\''+IP[0]+'\''+' AND PORT='+'\''+IP[1]+'\''
                print SQL
                db = MySQLdb.connect("localhost", "root", "lq910816", "PythonDB", charset='utf8')
                cursor = db.cursor()
                cursor.execute(SQL)
                db.commit()
                cursor.close()
            except Exception,e:
                print e

def getIPFromDB():
    try:
        SQL = 'SELECT IP,PORT,TYPE FROM ip_proxies'
        db = MySQLdb.connect("localhost", "root", "lq910816", "PythonDB", charset='utf8')
        cursor = db.cursor()
        cursor.execute(SQL)
        ip = cursor.fetchall()
        return ip
    except Exception,e:
        print e
    finally:
        db.close()

if __name__ == '__main__':
    removeUselessIP()