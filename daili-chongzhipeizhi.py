from selenium import webdriver
from time import sleep
from PIL import Image, ImageEnhance
from pytesseract import *
import unittest


driver = webdriver.Chrome()
def yanzhengma():
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
    num = image_to_string(newVerify).replace(' ', '')  # 使用image_to_string识别验证码
    return num

"""财务管理-出入款配置"""
class churukuan(unittest.TestCase):
    def test_dailichongzhi(self):
        """代理充值配置"""
        driver.get('http://agent.wg-dns-prod16.com/#/login')
        c = 1
        while c == 1:
            text = yanzhengma()
            print(text)
            driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys('wg0006')
            driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys('a123456')
            driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
            sleep(1)
            driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
            sleep(2)
            try:
                """判断是否登陆成功"""
                if driver.find_element_by_xpath('//*[@class="usrInfo"]'):
                    c = 0
                    print(c)
            except:
                """登陆不成功后进行刷新"""
                driver.refresh()
                c = 1
                print(c)
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]').click()
        sleep(1)
        """进入出入款配置界面"""
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]/ul/li[7]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[1]/button[1]/span').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(
            "我是代理1号")
        driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[4]/div/div[2]/form/div[2]/div/div/input').send_keys(
            '123456789')
        # driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[4]/div/div[2]/form/div[3]/div/label/span[2]').click()
        driver.find_element_by_xpath(
            '//*[@id="pane-first"]/div/div[4]/div/div[2]/form/div[4]/div/label/span[2]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="pane-first"]/div/div[4]/div/div[2]/form/div[5]/div/div/div/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@class="el-button el-button--primary"]').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()
        sleep(3)
        """举报人设置"""
        driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[1]/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[5]/div/div[2]/form/div[1]/div/div/div/span/span').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()  #选择QQ号
        driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[5]/div/div[2]/form/div[2]/div/div[1]/input').clear()
        driver.find_element_by_xpath(
            '//*[@id="pane-first"]/div/div[5]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('123456789')
        driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[5]/div/div[3]/span/button[2]').click()
    def test_guangfangchongzhi(self):
        """官方充值配置"""
        driver.maximize_window()
        driver.get('http://agent.wg-dns-prod16.com/#/login')
        c = 1
        while c == 1:
            text = yanzhengma()
            print(text)
            driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys('wg0006')
            driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys('a123456')
            driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
            sleep(1)
            driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
            sleep(2)
            try:
                """判断是否登陆成功"""
                if driver.find_element_by_xpath('//*[@class="usrInfo"]'):
                    c = 0
                    print(c)
            except:
                """登陆不成功后进行刷新"""
                driver.refresh()
                c = 1
                print(c)
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]').click()
        sleep(1)
        """进入官方充值配置界面"""
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]/ul/li[7]').click()
        sleep(1)
        driver.find_element_by_id('tab-second').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[1]/button').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys("工商银行")
        driver.find_element_by_xpath(
            '//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[2]/div/div/input').send_keys("12345678912345678")
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[3]/div/div[1]/input').send_keys("菜鸟")
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[4]/div/div[1]/input').send_keys("工商银行")
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[5]/div/div[1]/div/div/div/input').send_keys("10")
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[5]/div/div[3]/div/div/div/input').send_keys("20000")
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[6]/div/label/span[1]/span').click()
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[7]/div/label/span[1]/span').click()
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[8]/div/div/div/span/span/i').click()
        sleep(1)
        # driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[8]/div/div/div/input').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="pane-second"]/div/div[4]/div/div[2]/form/div[9]/div/div/div/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@class="el-button el-button--primary"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    def test_xians(self):
        """线上入款配置"""
        driver.maximize_window()
        driver.get('http://agent.wg-dns-prod16.com/#/login')
        c = 1
        while c == 1:
            text = yanzhengma()
            print(text)
            driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys('wg0006')
            driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys('a123456')
            driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
            sleep(1)
            driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
            sleep(2)
            try:
                """判断是否登陆成功"""
                if driver.find_element_by_xpath('//*[@class="usrInfo"]'):
                    c = 0
                    print(c)
            except:
                """登陆不成功后进行刷新"""
                driver.refresh()
                c = 1
                print(c)
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]').click()
        sleep(1)
        """进入官方充值配置界面"""
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]/ul/li[7]').click()
        sleep(1)
        driver.find_element_by_id('tab-third').click()
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[1]/button[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[1]/div/div/div/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[4]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[2]/div/div/div[1]/span/span/i').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[6]').click()
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[3]/div/div/input').send_keys('赢赢支付支付宝')
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[4]/div/div/input').send_keys('80000024')
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[5]/div/div/input').send_keys('7C97A814592B4B598BDB1DB9F829FFC0')
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[7]/div/div/input').send_keys('prerelease-payment.leyingpaysys.com')
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[8]/div/div[1]/div/div/div/input').send_keys(10)
        driver.find_element_by_xpath(
            '//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[8]/div/div[3]/div/div/div/input').send_keys(6999)
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[9]/div/label/span[1]/span').click()
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[10]/div/label/span[1]/span').click()
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[2]/form/div[11]/div/div/div[1]/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="pane-third"]/div/div[4]/div/div[3]/span/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    def test_xianc(self):
        driver.maximize_window()
        driver.get('http://agent.wg-dns-prod16.com/#/login')
        c = 1
        while c == 1:
            text = yanzhengma()
            print(text)
            driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys('wg0006')
            driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys('a123456')
            driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
            sleep(1)
            driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
            sleep(2)
            try:
                """判断是否登陆成功"""
                if driver.find_element_by_xpath('//*[@class="usrInfo"]'):
                    c = 0
                    print(c)
            except:
                """登陆不成功后进行刷新"""
                driver.refresh()
                c = 1
                print(c)
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]').click()
        sleep(1)
        """进入官方充值配置界面"""
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]/ul/li[7]').click()
        sleep(1)
        driver.find_element_by_id('tab-fifth').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[1]/button').click()
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[1]/div/div/div/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[2]/div/div/input').send_keys("汇淘支付出款")
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[3]/div/div/input').send_keys("M32266295")
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[4]/div/div/input').send_keys(
            "3c30cb7d7521e7b87eb8f4b1e9fa9307")
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[5]/div/div/input').send_keys(
            "3c30cb7d7521e7b87eb8f4b1e9fa9307")
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[6]/div/div/input').send_keys(
            "prerelease-remit.leyingpaysys.com")
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[6]/div/div/input').send_keys(
            "prerelease-remit.leyingpaysys.com")
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[7]/div/div[1]/div/div/div/div/div[1]/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]').click()
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[7]/div/div[2]/div/div/div/div/input').send_keys(5)
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[8]/div/div[1]/div/div/div/div/div[1]/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]').click()
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[8]/div/div[2]/div/div/div/div/input').send_keys(5)
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[9]/div/div/div[1]/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[10]/div/div[1]/div/div/div/input').send_keys(10)
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[10]/div/div[3]/div/div/div/input').send_keys(30000)
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[11]/div/label/span[1]/span').click()
        driver.find_element_by_xpath('//*[@id="pane-fifth"]/div/div[4]/div/div[2]/form/div[12]/div/div/div[1]/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@class="el-button el-button--primary"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    def test_chukuai(self):
        """线上出款配置"""
        driver.maximize_window()
        driver.get('http://agent.wg-dns-prod16.com/#/login')
        c = 1
        while c == 1:
            text = yanzhengma()
            print(text)
            driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys('wg0006')
            driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys('a123456')
            driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
            sleep(1)
            driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
            sleep(2)
            try:
                """判断是否登陆成功"""
                if driver.find_element_by_xpath('//*[@class="usrInfo"]'):
                    c = 0
                    print(c)
            except:
                """登陆不成功后进行刷新"""
                driver.refresh()
                c = 1
                print(c)
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]').click()
        sleep(1)
        """进入官方充值配置界面"""
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]/ul/li[7]').click()
        sleep(1)
        driver.find_element_by_id('tab-fourth').click()
        driver.find_element_by_xpath('//*[@id="pane-fourth"]/div/form/div[1]/div/div/div[2]/div[2]/div/div/input').send_keys(10)
        driver.find_element_by_xpath('//*[@id="pane-fourth"]/div/form/div[1]/div/div/div[2]/div[3]/div/div/input').send_keys(10000)
        driver.find_element_by_xpath('//*[@id="pane-fourth"]/div/form/div[1]/div/div/div[2]/div[4]/div/div/textarea').send_keys('一百万个可能')
        driver.find_element_by_xpath('//*[@id="pane-fourth"]/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div/input').send_keys(10)
        driver.find_element_by_xpath('//*[@id="pane-fourth"]/div/form/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@class="el-button el-button--primary"]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    def test_guma(self):
        """固码入款配置"""
        driver.maximize_window()
        driver.get('http://agent.wg-dns-prod16.com/#/login')
        c = 1
        while c == 1:
            text = yanzhengma()
            print(text)
            driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys('wg0006')
            driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys('a123456')
            driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
            sleep(1)
            driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
            sleep(2)
            try:
                """判断是否登陆成功"""
                if driver.find_element_by_xpath('//*[@class="usrInfo"]'):
                    c = 0
                    print(c)
            except:
                """登陆不成功后进行刷新"""
                driver.refresh()
                c = 1
                print(c)
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]').click()
        sleep(1)
        """进入官方充值配置界面"""
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]/ul/li[7]').click()
        sleep(1)
        driver.find_element_by_id('tab-sixth').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-sixth"]/div/div[1]/button').click()
        driver.find_element_by_xpath('//*[@id="pane-sixth"]/div/div[4]/div/div[2]/form/div[1]/div/div/div/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="pane-sixth"]/div/div[4]/div/div[2]/form/div[2]/div/div/input').send_keys('支付宝收款')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-sixth"]/div/div[4]/div/div[2]/form/div[3]/div/div/div/div[1]/input').send_keys('D:/tupian/0008.jpg')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="pane-sixth"]/div/div[4]/div/div[2]/form/div[4]/div/div[1]/div/div/div/input').send_keys(10)
        driver.find_element_by_xpath('//*[@id="pane-sixth"]/div/div[4]/div/div[2]/form/div[4]/div/div[3]/div/div/div/input').send_keys(10000)
        driver.find_element_by_xpath('//*[@id="pane-sixth"]/div/div[4]/div/div[2]/form/div[6]/div/label/span[1]/span').click()
        driver.find_element_by_xpath('//*[@id="pane-sixth"]/div/div[4]/div/div[2]/form/div[7]/div/div/div[1]/span/span/i').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@class="el-button el-button--primary"]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@class="el-button el-button--default el-button--small el-button--primary "]').click()
test = unittest.TestSuite()
test.addTest(churukuan("test_dailichongzhi"))
# test.addTest(churukuan("test_guangfangchongzhi"))
# test.addTest(churukuan("test_xians"))
# test.addTest(churukuan("test_xianc"))
# test.addTest(churukuan("test_chukuai"))




