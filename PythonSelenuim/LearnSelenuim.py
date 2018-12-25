#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

from selenium import webdriver
#调用键盘按键操作
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.douban.com')
print driver.title
driver.find_element_by_name('q').send_keys(u'电影')
# driver.find_element_by_class_name()
# driver.find_element_by_css_selector('//span[@class]')
input1 = driver.find_element_by_xpath("//span[@class='bn']/input")
ActionChains(driver).move_to_element(input1).click(input1).perform()


