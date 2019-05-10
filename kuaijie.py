from tkinter import *
from tkinter import scrolledtext,messagebox
from selenium import webdriver
from time import sleep
from PIL import Image, ImageEnhance
from pytesseract import *
from tkinter import ttk


wangzhi ={}
wangzhi['总控'] =['http://control.wg-dns-prod.com/index','admin','123456']
wangzhi['棋牌188'] =['http://agent.wg-dns-prod14.com/#/login','wg0004','a123456']
wangzhi['辉煌007'] =['http://agent.wg-dns-prod9.com/#/login','huihuang07','a123456']
wangzhi['姚记'] =['http://agent11.wg-dns-prod.com/#/login','yaoji001','a123456']
wangzhi['波克'] =['http://agent6.wg-dns-prod.com/#/login','boke001','a123456']
wangzhi['万国'] =['http://agent3.wg-dns-prod.com/#/login','wg0001','a123456']
wangzhi['掌上'] =['http://agent12.wg-dns-prod.com/#/login','wg0002','a123456']
wangzhi['乐点'] =['http://agent5.wg-dns-prod.com/#/login','ledian001','a123456']
wangzhi['测试环境'] =['http://agent.huihuang300.com/#/login','q00001','qwaszx12']
youxi ={}
youxi['牛牛'] ='http://www.nn.com'
youxi['棋牌188'] ='http://www.wg-dns-prod14.com/#/login'
youxi['辉煌007'] ='http://www.wg-dns-prod9.com/#/login'
youxi['姚记'] ='http://www11.wg-dns-prod.com/#/login'
youxi['波克'] ='http://www6.wg-dns-prod.com/#/login'
youxi['万国'] ='http://www3.wg-dns-prod.com/#/login'
youxi['掌上'] ='http://www12.wg-dns-prod.com/#/login'
youxi['欢乐棋牌'] ='http://www10.wg-dns-prod.com/#/login'
youxi['乐点'] ='http://www5.wg-dns-prod.com/#/login'
xians ={}
"""线上网址"""
xians['牛牛'] ='http://www.nn.com'
xians['棋牌188'] ='http://www.qp188.com'
xians['辉煌007'] ='http://www.6322.com'
xians['姚记'] ='http://www.yj7799.com'
xians['波克'] ='http://www.bokqp.com'
xians['万国'] ='http://www.wgqp.cc'
xians['掌上'] ='http://www.6267.com'
xians['乐点'] ='http://www.53598.com/#/login'
xians['多玩'] ='http://www.dwqp.com/#/login'
# xians['掌上'] ='http://www12.wg-dns-prod.com/#/login'
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
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(wangzhi[numberChosen.get()][0])
    sleep(1)
    c = 1
    while c == 1:
        if numberChosen.get()=='总控':
            driver.save_screenshot('verifyCode.png')  # 截取当前网页，该网页有我们需要的验证码
            # 定位验证码
            sleep(1)
            imgelement = driver.find_element_by_id("codeImg")
            # 获取验证码x,y轴坐标
            location = imgelement.location
            # 获取验证码的长宽
            size = imgelement.size
            print(location, size)
            # 写成我们需要截取的位置坐标
            rangle = (
                int(location['x']), int(location['y']), int(location['x'] + size['width']),
                int(location['y'] + size['height']))
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
            sleep(1)
            driver.find_element_by_id('username').send_keys(wangzhi[numberChosen.get()][1])
            driver.find_element_by_id('password').send_keys(wangzhi[numberChosen.get()][2])
            driver.find_element_by_id('code').send_keys(num)
            driver.find_element_by_id('login').click()
            try:
                if driver.find_element_by_xpath('//*[@class="logo-text shine"]'):
                    c = 0
                    print(c)
            except:
                """登陆不成功后进行刷新"""
                driver.refresh()
                c = 1
                print(c)
        else:
            text = yanzhengma()
            print(text)
            driver.find_element_by_xpath('//*[@placeholder="账号"]').send_keys(wangzhi[numberChosen.get()][1])
            driver.find_element_by_xpath('//*[@placeholder="密码"]').send_keys(wangzhi[numberChosen.get()][2])
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
def button2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(youxi[numberChosen001.get()])
def button3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(xians[numberChosen002.get()])
def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y
jiemian = Tk()
jiemian.title("乐赢")
a, b = jiemian_info()
jiemian.geometry("400x400+%d+%d" % (a, b))

Label(text="代理PC：").place(x=50,y=25)
Label(text="开版PC：").place(x=50,y=90)
Label(text="线上PC：").place(x=50,y=150)
numberChosen=ttk.Combobox(width=10,font=('微软雅黑', 10))
numberChosen.place(x=100,y=25)
numberChosen['values'] = ["棋牌188","辉煌007","姚记","波克","万国","掌上","乐点","总控",'测试环境']
numberChosen.current(0)
numberChosen001=ttk.Combobox(width=10,font=('微软雅黑', 10))
numberChosen001.place(x=100,y=90)
numberChosen001['values'] = ["棋牌188","辉煌007","姚记","波克","万国","掌上","欢乐棋牌","乐点"]
numberChosen001.current(0)
numberChosen002=ttk.Combobox(width=10,font=('微软雅黑', 10))
numberChosen002.place(x=100,y=150)
numberChosen002['values'] = ["牛牛","棋牌188","辉煌007","姚记","波克","万国","掌上","乐点",'多玩']
numberChosen002.current(0)
# Label(text="账号：").place(x=60,y=60)
# Label(text="密码：").place(x=60,y=90)
# var_usr = StringVar()
# var_pwd = StringVar()
# url = Entry( textvariable=var_usr, font=('微软雅黑', 10),width=12)
# url.place(x=100,y=60)
# pwd = Entry( textvariable=var_pwd, font=('微软雅黑', 10),width=12)
# pwd.place(x=100,y=90)
Button(text="登录", width=13,command=button1).place(x=220, y=25)
Button(text="打开", width=13,command=button2).place(x=220, y=90)
Button(text="打开", width=13,command=button3).place(x=220, y=150)


jiemian.mainloop()