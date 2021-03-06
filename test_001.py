from selenium import webdriver
from time import sleep
from PIL import Image, ImageEnhance
# import baseinfo
from pytesseract import *

chenggong=0
shibai=0

for i in range(10):
    driver = webdriver.Chrome()
    driver.get('http://agent.huihuang300.com/#/login')
    sleep(1)
    driver.refresh()
    driver.save_screenshot('verifyCode.png')  # 截取当前网页，该网页有我们需要的验证码
    # 定位验证码
    sleep(1)
    imgelement = driver.find_element_by_xpath("//*[@class='codeimg']")
    # 获取验证码x,y轴坐标
    location = imgelement.location
    # 获取验证码的长宽
    size = imgelement.size
    print(location, size)
    # 写成我们需要截取的位置坐标
    rangle = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
    # 打开截图
    i = Image.open('verifyCode.png')
    # 使用Image的crop函数，从截图中再次截取我们需要的区域
    imgry = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域

    imgry.save('getVerifyCode.png')

    im = Image.open('getVerifyCode.png')

    im = im.convert('L')  # 图像加强，二值化

    sharpness = ImageEnhance.Contrast(im)  # 对比度增强

    sharp_img = sharpness.enhance(2.0)

    sharp_img.save("newVerifyCode.png")

    newVerify = Image.open('newVerifyCode.png')
    # 使用image_to_string识别验证码
    text = image_to_string(newVerify).replace(' ', '')  # 使用image_to_string识别验证码
    print(text)

    driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys('test102')
    driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys('a123456')
    driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
    sleep(1)
    driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
    sleep(2)
    try:
        if driver.find_element_by_xpath('/html/body/div[2]'):
            shibai = shibai + 1
            driver.refresh()
    except:
        if driver.find_element_by_xpath('//*[@class="logo"]'):
            chenggong = chenggong + 1
    finally:
        driver.quit()
print(shibai,chenggong)


# driver.quit()

#test102/a123456