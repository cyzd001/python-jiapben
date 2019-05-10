from appium import webdriver
import time
from PIL import Image, ImageEnhance
# import baseinfo
from pytesseract import *
desired_caps = {
    #设备系统
    'platformName': 'Android',
    #设备名称
    'deviceName': '127.0.0.1:7555',
    #安卓版本
    'platformVersion': '6.0.1',
    # apk包名
    'appPackage': 'org.cocos2d.huihuang07_openVersion',
    # apk的launcherActivity
    'appActivity': 'org.cocos2dx.javascript.AppActivity',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
     'resetKeyboard':True,# 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(25)
# text = driver.contexts
# print(text)
# print(newVerify.text)
# 使用image_to_string识别验证码
# driver.find_element_by_xpath('//android.widget.FrameLayout[@text="账号登录"]').click()
driver.tap([(1050,643)])
time.sleep(3)
driver.save_screenshot('verifyCode.png')
rangle = (830,279,985,326)
i = Image.open('verifyCode.png')
#使用Image的crop函数，从截图中再次截取我们需要的区域
imgry=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
imgry.save('getVerifyCode.png')
im=Image.open('getVerifyCode.png')
im = im.convert('L')#图像加强，二值化
sharpness =ImageEnhance.Contrast(im)#对比度增强
sharp_img = sharpness.enhance(2.0)
sharp_img.save("newVerifyCode.png")
newVerify = Image.open('newVerifyCode.png')
# 使用image_to_string识别验证码
text=image_to_string(newVerify).replace(' ', '') #使用image_to_string识别验证码
time.sleep(1)
print(text)