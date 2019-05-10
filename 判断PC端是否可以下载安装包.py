from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.53598.com/')
sleep(1)
try:
    driver.find_element_by_id('androidClick').click()
    print("下载apk包OK")
except:
    print("下载apk包失败")
try:
    driver.find_element_by_id('iosClick').click()
    print("下载ipa包OK")
except:
    print("下载ipa包失败")
nowhandle = driver.current_window_handle  #获取当前网页句柄
driver.find_element_by_xpath('//*[@class="kefuBox"]').click()
allhandles = driver.window_handles
# for link in driver.find_elements_by_xpath('//*[@href]'):
#     # print (link.get_attribute('href'))
#     if 'http://www.wg-dns-prod9.com/huihuang07_openVersion-release-signed.apk' == link.get_attribute('href'):
#         print("下载apk安装包失败，后台没有配置安装包")
#     elif 'http://www.wg-dns-prod9.com/huihuang07_open.ipa' == link.get_attribute('href'):
#         print("下载ios安装包失败，后台没有配置安装包")
if len(allhandles)==1:
    print("打开客服界面失败，请排查原因")
elif len(allhandles)==2:
    print("打开客服界面成功")
    driver.switch_to.window(allhandles[1])  #跳转到客服页面
    print("客服页面："+driver.current_url)
for i in allhandles:
    if nowhandle !=i:
        print("打开客服页面成功")
        driver.switch_to.window(i)
        print(driver.current_url)
# driver.quit()
# http://www.wg-dns-prod9.com/huihuang07_openVersion-release-signed.apk
#http://www.wg-dns-prod9.com/huihuang07_open.ipa
# http://prod-android.huihuang200.com/128810/phone/huihuang07_open.ipa
# http://prod-android.huihuang200.com/128810/phone/huihuang07_openVersion-release-signed.apk




# https://chat.livechatvalue.com/chat/chatClient/chatbox.jsp?companyID=1025023&configID=73813&jid=9023486389&s=1
