from selenium import webdriver
from time import sleep
from PIL import Image, ImageEnhance
# import baseinfo
from pytesseract import *

driver= webdriver.Chrome()
driver.get('http://agent.huihuang300.com/#/login')
driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys('test102')
driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys('a123456')
# driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
sleep(1)
# driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()