#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
from selenium import webdriver
#调用键盘按键操作
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

# driver  = webdriver.Chrome()
# driver.get('https://www.cnblogs.com/derek1184405959/p/8449159.html#')
# action1 = driver.find_element_by_xpath("//div[@id='test33']/ul/div[5]/a")
# # action1 = driver.find_element_by_css_selector('a':contains('Python进阶'))
# # ActionChains(driver).move_to_element(action1).perform()
# select = Select(driver.find_element_by_xpath("//div[@id='test33']/ul/div[5]/div"))
# select.select_by_index(2)

driver = webdriver.Chrome()
driver.get('https://passport.zhaopin.com/login')
print driver.get_cookie()

