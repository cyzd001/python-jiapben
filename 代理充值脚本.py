from tkinter import *
from tkinter import scrolledtext,messagebox
from selenium import webdriver
from time import sleep
from PIL import Image, ImageEnhance
from pytesseract import *
from tkinter import ttk
from tkinter import messagebox
import re

wangzhi ={}
wangzhi['总控'] ='http://control.wg-dns-prod.com/index'
wangzhi['棋牌188'] =['http://agent.wg-dns-prod14.com/#/login','wg0004','a123456']
wangzhi['辉煌007'] =['http://agent.wg-dns-prod9.com/#/login','huihuang01','a123456']
wangzhi['姚记'] =['http://agent11.wg-dns-prod.com/#/login','yaoji001','a123456']
wangzhi['波克'] =['http://agent6.wg-dns-prod.com/#/login','boke001','a123456']
wangzhi['万国'] =['http://agent3.wg-dns-prod.com/#/login','wg0001','a123456']
wangzhi['掌上'] =['http://agent12.wg-dns-prod.com/#/login','wg0002','a123456']
wangzhi['91棋牌'] =['http://agent10.wg-dns-prod13.com/#/login','huanle001','a123456']

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
def button1():
    global driver
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    if money.get().isdigit():
        driver = webdriver.Chrome()  #chrome_options=option
        driver.maximize_window()
        driver.get(wangzhi[numberChosen.get()][0])
        c = 0
        while c == 0:
            text = yanzhengma()
            print(text)
            driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys(wangzhi[numberChosen.get()][1])
            driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys(wangzhi[numberChosen.get()][2])
            driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
            sleep(1)
            driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
            sleep(1)
            try:
                """判断是否登陆成功"""
                if driver.find_element_by_xpath('//*[@class="usrInfo"]'):
                    c = 1
            except:
                """登陆不成功后进行刷新"""
                driver.refresh()
                # driver.find_element_by_xpath('//*[@class="codeimg"]').click()
                c = 0
                # text = yanzhengma()
                # print(text)
                # driver.find_element_by_xpath('//*[@placeholder="请输入右侧验证码"]').send_keys(text)
                # driver.find_element_by_xpath('//*[@class="el-button el-button--success"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]').click()
        sleep(1)
        """进入出入款配置界面"""
        driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[2]/ul/li[4]/ul/li[1]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/section/div/div[2]/div[2]/form/div[1]/div/div/input').send_keys(
            usr.get())
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/section/div/div[2]/div[2]/form/div[1]/div/div/div/button').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/section/div/div[2]/div[2]/form/div[4]/div/div[1]/input').send_keys(
            money.get())
        driver.find_element_by_xpath('//*[@class="el-textarea__inner"]').send_keys("充%r钱了" % money.get())
        driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/section/div/div[2]/div[2]/form/div[7]/div/div/button[2]').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
        messagebox.showinfo('提示', '充值成功')
        driver.quit()
    else:
        messagebox.showinfo('提示', '请输入符合要求金额')

def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y
jiemian = Tk()
jiemian.title("乐赢充值")
a, b = jiemian_info()
jiemian.geometry("400x400+%d+%d" % (a, b))

Label(text="代理：").place(x=60,y=25)
Label(text="会员：").place(x=60,y=65)
Label(text="金额：").place(x=60,y=105)
numberChosen=ttk.Combobox(width=10,font=('微软雅黑', 10))
numberChosen.place(x=100,y=25)
numberChosen['values'] = ["91棋牌","棋牌188","辉煌007","姚记","波克","万国","掌上","总控"]
numberChosen.current(0)
var_usr = StringVar()
usr = Entry( textvariable=var_usr, font=('微软雅黑', 10),width=12)
usr.place(x=100,y=65)
var_money = IntVar
money = Entry(textvariable=var_money, font=('微软雅黑', 10),width=12)
money.place(x=100,y=105)

Button(text="充值", width=13,command=button1).place(x=100, y=140)

if __name__ == '__main__':
    jiemian.mainloop()
