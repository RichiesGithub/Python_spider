#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import requests
from fake_useragent import UserAgent
from lxml import etree
import datetime
import MySQLdb

class spider_IP:
    def __init__(self):
        self.Switch = True
        self.page = 4

    def get_ip(self,url):
        global now_date,str_now_date,str_yes_date
        now_date = datetime.datetime.now()
        str_now_date = (datetime.datetime.now().strftime('%Y-%m-%d'))[2:]
        str_yes_date = ((now_date + datetime.timedelta(-1)).strftime('%Y-%m-%d'))[2:]
        # str_y_yes_date = ((now_date + datetime.timedelta(-2)).strftime('%Y-%m-%d'))[2:]

        ua= UserAgent()
        headers = {"User-Agent": ua.random}
        response = requests.get(url,headers=headers).text.encode('utf-8')
        contents = etree.HTML(response)
        content  = contents.xpath('//table[@id="ip_list"]')[0]
        trs = content.xpath('//tr')[1:][2]
        ips = trs.xpath('//td[2]/text()')
        port = trs.xpath('//td[3]/text()')
        type = trs.xpath('//td[6]/text()')
        speed = trs.xpath('//td[7]/div/@title')
        checktime = trs.xpath('//td[10]/text()')
        if checktime[0][:8] == str_now_date or checktime[0][:8] == str_yes_date:
            data = [ips,port,type,speed,checktime]
            self.washIP(data)
        else:
            self.Switch = False

    def washIP(self,data):
        global values
        global value
        values = []
        i=0
        for time in data[3]:
            if (float(time.encode('utf-8')[:-3]) <= 1) and (data[4][0][:8] == str_now_date or data[4][0][:8] == str_yes_date):
                value =(data[0][i],data[1][i].encode('utf-8'),data[2][i].encode('utf-8'),data[3][i].encode('utf-8'),data[4][i].encode('utf-8'))
                values.append(value)
            i += 1
        self.saveData(values)

    def saveData(self,value):
        SQL = 'INSERT INTO ip_proxies(IP,PORT,TYPE,SPEED,CHECK_TIME) VALUES(%s,%s,%s,%s,%s)'
        try:
            print '正在写入数据到数据库...'
            db = MySQLdb.connect("localhost", "root", "lq910816", "PythonDB", charset='utf8')
            cursor = db.cursor()
            cursor.executemany(SQL,value)
            db.commit()
            print '写入成功。'

        except Exception, e:
            db.rollback()
            print e

    def startWork(self):
        halfurl = 'https://www.xicidaili.com/nn/'
        while self.Switch == True:
            url = halfurl+str(self.page)
            self.get_ip(url)
            self.page+=1
        print'IP 获取完成。'

if __name__ == '__main__':
    startwork = spider_IP()
    startwork.startWork()