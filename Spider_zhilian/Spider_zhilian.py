#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import requests
import urllib
import json
import re
from lxml import etree
import MySQLdb
from fake_useragent import UserAgent

class Spider_zhilian:

    def __init__(self):
        self.page=0
        self.Switch = True

    def spider(self,page,city,kw):
        param={
            'start': page,
            'pageSize': 60,
            'cityId': city,
            'workExperience': -1,
            'education': -1,
            'companyType': -1,
            'employmentType': -1,
            'jobWelfareTag': -1,
            'kw': kw,
            'kt': 3,
            'lastUrlQuery': {"p": page, "pageSize": "60", "jl": city, "kt": "3","kw":kw}
        }
        ua=UserAgent()
        headers = {
            'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.5,zh-HK;q=0.3,en;q=0.2',
            # 'Connection':'keep-alive',
            'Connection': 'close',
            'Cookie':'urlfrom2=121126445; adfbid2=0;…3d7240-1327104-167a10d62c7211',
            'Host':'fe-api.zhaopin.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':str(ua)
            }
        url = 'https://fe-api.zhaopin.com/c/i/sou?'+urllib.urlencode(param)
        data = requests.get(url,headers=headers).text.encode('utf-8')
        with open('zhaopin.json','w') as f:
            f.write(data)
            f.close()
        self.dataWash()

    def datailsPageSpider(self,url):
        headers = {
            'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.5,zh-HK;q=0.3,en;q=0.2',
            # 'Connection': 'keep-alive',
            'Connection': 'close',
            'Cookie': 'urlfrom2=121126445; adfbid2=0;…3d7240-1327104-167a10d62c7211',
            'Host': 'jobs.zhaopin.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64;x64;rv:63.0) Gecko/20100101 Firefox/63.0'
        }
        html = requests.get(url,headers=headers).text
        content = etree.HTML(html)
        neednumber = content.xpath("//div[@class='info-three l']/span[4]")[0].text.encode('utf-8')
        joblocal = content.xpath("//div[@class='info-three l']/span[1]/a")[0].text.encode('utf-8')
        print joblocal
        joblight = re.search(r'.*JobWelfareTab = \'(.*?)\'', html).group(1).encode('utf-8')
        jobdesc = str(content.xpath("//div[@class='responsibility pos-common']/div[@class='pos-ul']")[0].xpath('string(.)').encode('utf-8'))
        detailsdict={'neednumber':neednumber,'joblocal':joblocal,'joblight':joblight,'jobdesc':jobdesc}
        return detailsdict
    def dataWash(self):
        onepagedata=[]
        with open('zhaopin.json','r') as f:
            line = f.readline()
        result = json.loads(line)
        items = result['data']['results']
        for item in items:
            Jobtitle=item['jobName']
            Jobtype = item['jobType']['display']
            Salary=item['salary']
            experience=item['workingExp']['name']
            empltype = item['emplType']
            education = item['eduLevel']['name']
            companyname=item['company']['name']
            companytype=item['company']['type']['name']
            companysize=item['company']['size']['name']
            jobdetailslink = item['positionURL']
            detailspage = self.datailsPageSpider(jobdetailslink)
            mainpagedata={'Jobtitle':Jobtitle,'Jobtype':Jobtype,'Salary':Salary,'experience':experience,'empltype':empltype,'education':education,'companyname':companyname
                ,'companytype':companytype,'companysize':companysize,'jobdetailslink':jobdetailslink}
            alldata=dict(mainpagedata,**detailspage)
            onepagedata.append(alldata)
        self.dataSave(onepagedata)
    def dataSave(self,data):
        values=[]
        for item in data:
            value=((item['Jobtitle'],item['companyname'],item['companytype'],item['companysize'],item['Jobtype'],item['Salary'],item['experience']
                    ,item['empltype'],item['education'],item['jobdetailslink'],item['neednumber'],item['joblocal'],item['joblight'],item['jobdesc']))
            values.append(value)
        sql = 'INSERT INTO spider_zhilian(JOBTITLE,COMPANYNAME,COMPANYTYPE,COMPANYSIZE,JOBTYPE,SALARY,EXPERIENCE,EMPLTYPE,EDUCATION,DETAILSLINK,NEEDNUM,JONLOCAL,JOBLIGHT,JOBDESC) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            print '正在写入数据到数据库...'
            db = MySQLdb.connect("localhost", "root", "lq910816", "PythonDB", charset='utf8')
            cursor = db.cursor()
            cursor.executemany(sql, values)
            db.commit()
            print '写入成功。'
        except Exception, e:
            db.rollback()
            print e
    def startWork(self,endpage,city,kw):
        while endpage>0:
            print'正在爬取第 '+str(self.page/60+1)+' 页数据'
            self.spider(self.page,city,kw)
            self.page+=1*60
            endpage -= 1
        print 'thanks for used'
if __name__ == '__main__':
    endpage = int(raw_input('请输入结束页：'))
    city = raw_input('请输入城市名称：')
    kw = raw_input('请输入关键词：')
    spider = Spider_zhilian()
    spider.startWork(endpage,city,kw)