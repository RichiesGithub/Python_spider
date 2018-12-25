#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup
import json
import MySQLdb
class SpiderBS4:

    def __init__(self):
        pass

    def loadPage(self,url):
        req = urllib2.Request(url + 'position.php?&start=10#a')
        html = urllib2.urlopen(req).read()
        soup = BeautifulSoup(html,'lxml')
        soup.stripped_strings
        result1 = soup.find_all(class_='odd')
        result2 = soup.find_all(class_='even')
        result = result1+result2
        Jobs=[]
        for item in result:
            # #方法一， 用基础方法查找
            # list =  item.find_all('td')
            # print list
            # JobNmae = list[0].a.get_text()
            # # link = url+list.contents[1].a.get('href')
            # link = url + list[0].a['href']
            # Jobstyle = list[1].string
            # NeedNum = list[2].string
            # Location = list[3].string
            # PushTime = list[4].string
            # items = {'JobNmae':JobNmae,'link':link,'Jobstyle':Jobstyle,'NeedNum':NeedNum,'Location':Location,'PushTime':PushTime}
            # Jobs.append(items)

            #方法二，用CSS 选择器查找
            JobNmae = item.select('a')[0].get_text()
            link = url + item.select('a')[0].attrs['href']
            Jobstyle = item.select('td')[1].string
            NeedNum = item.select('td')[2].string
            Location = item.select('td')[3].string
            PushTime = item.select('td')[4].string
            items = {'JobNmae': JobNmae, 'link': link, 'Jobstyle': Jobstyle, 'NeedNum': NeedNum, 'Location': Location,'PushTime': PushTime}
            Jobs.append(items)
        line =json.dumps(Jobs,ensure_ascii=False)
        with open('tencent.json','a') as f:
            f.write(line.encode('utf-8'))
        self.writeDatatoDB()
    def dealData(self):
        pass

    def writeDatatoDB(self):
        values=[]
        with open('tencent.json','r') as f:
            list = f.read()
            data = json.loads(list)
        for dict in data:
            value =((dict['JobNmae'],dict['link'],dict['Jobstyle'],int(dict['NeedNum']),dict['Location'],dict['PushTime']))
            values.append(value)
        sql = 'INSERT INTO tencentjson(JOBNAME,LINK,JOBTYPE,NUM,LOCAL,DATA) VALUES (%s,%s,%s,%s,%s,%s)'
        try:
            db = MySQLdb.connect("localhost", "root", "lq910816", "PythonDB", charset='utf8')
            cursor = db.cursor()
            cursor.executemany(sql,values)
            db.commit()
        except Exception,e:
            db.rollback()
            print e

    def startWork(self):
        url = 'https://hr.tencent.com/'
        self.loadPage(url)


if __name__ == '__main__':

    spider = SpiderBS4()
    spider.startWork()