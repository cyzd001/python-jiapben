from tkinter import *
from selenium import webdriver
import tkinter as tk
from tkinter import scrolledtext,messagebox
from time import sleep
from tkinter import ttk
import xlrd
import requests
import json
import qrcode
def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y
jiemian = Tk()
jiemian.title("测试装备")
a, b = jiemian_info()
# jiemian.geometry("800x600+%d+%d" % (a, b))
class login(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("300x150+%d+%d" % (a, b)) # 设置窗口大小
        self.urll = 'http://192.168.18.38:8073/login'
        self.createPage()
    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        # Label(self.page).grid(row=0, stick=W)
        Label(self.page, text="用户：").grid(row=0, column=0, stick=E,pady=10)
        Label(self.page, text="账号：").grid(row=1, column=0, stick=E)
        '''设置文本框'''
        self.url = Entry(self.page, font=('微软雅黑', 10), width=15)
        self.url.grid(row=0, column=1, stick=E,pady=10)
        # var_pwd = StringVar()
        self.pwd = Entry(self.page, font=('微软雅黑', 10), width=15)
        self.pwd.grid(row=1, column=1, stick=E)
        '''设置按钮'''
        Button(self.page, text="登录", width=10, command=self.button1).grid(row=2, column=1, stick=W+E,pady=10)
    def button1(self):
        datain = {'SJH': self.url.get(), 'PWD': self.pwd.get()}
        # num = int(url.get())
        # print(type(num))
        # print(datain)
        m = requests.get(url=self.urll, data=datain)
        # print(m.text)
        # print(type(eval(m.text)))
        msg = eval(m.text)
        if msg['msg_code'] == '200':
            messagebox.showinfo('提示', '成功登录')
            self.page.destroy()
            mainpage(self.root)
        elif msg['msg_code'] == '204':
            messagebox.showinfo('提示', '密码和用户名错误')
            self.page.pack()
class mainpage(object):
    def __init__(self, master=None):
        self.root= master  # 定义内部变量root
        self.root.geometry("800x600+%d+%d" % (a, b))
        self.createPage()
    def createPage(self):
        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.queryPage = QueryFrame(self.root)
        self.dingcanpage = dingcanFrame(self.root)
        self.jiekoupage = jiekouFrame(self.root)
        self.erweima = EWMFrame(self.root)
        self.inputPage.pack()  # 默认显示数据录入界面
        menubar = Menu(jiemian)
        fmenu1 = Menu(jiemian, tearoff=0)
        fmenu2 = Menu(jiemian, tearoff=0)
        for item in ['网站', '构建','接口', '生成二维码','订餐']:
            if item == '网站':
                fmenu1.add_command(label=item,command=self.inputData)
                fmenu1.add_separator()
            elif item == '构建':
                fmenu1.add_command(label=item,command=self.queryData)
                """添加横线"""
                fmenu1.add_separator()
            elif item =='接口':
                fmenu1.add_command(label=item,command=self.jiekou)
                """添加横线"""
                fmenu1.add_separator()
            elif item =='生成二维码':
                fmenu1.add_command(label=item,command=self.erweim)
                """添加横线"""
                fmenu1.add_separator()
            else:
                fmenu1.add_command(label=item,command=self.dingcan)
        for item in ['帮助','退出']:
            fmenu2.add_command(label=item, command=self.tuchu)
            if item != '退出':
                """添加横线"""
                fmenu2.add_separator()
        menubar.add_cascade(label="选项",menu=fmenu1)
        menubar.add_cascade(label="操作",menu=fmenu2)
        self.root['menu'] = menubar
    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.dingcanpage.pack_forget()
        self.jiekoupage.pack_forget()
        self.erweima.pack_forget()
    def queryData(self):
        self.queryPage.pack()
        self.inputPage.pack_forget()
        self.dingcanpage.pack_forget()
        self.jiekoupage.pack_forget()
        self.erweima.pack_forget()
    def dingcan(self):
        self.erweima.pack_forget()
        self.dingcanpage.pack()
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.jiekoupage.pack_forget()
    def jiekou(self):
        self.erweima.pack_forget()
        self.jiekoupage.pack()
        self.dingcanpage.pack_forget()
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
    def erweim(self):
        self.erweima.pack()
        self.jiekoupage.pack_forget()
        self.dingcanpage.pack_forget()
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
    def tuchu(self):
       """退出按钮"""
       a = messagebox.askokcancel('提示', '真的要退出吗？')
       print(a)
       if a == True:
           jiemian.quit()  # 关闭窗口
           jiemian.destroy()  # 将所有的窗口小部件进行销毁，应该有内存回收的意思
class InputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.var_usr = StringVar()
        self.var_pwd = StringVar()
        self.var_xm = StringVar()
        self.createPage()
    def createPage(self):
        Label(self, text="网站：").grid(row=0, column=0,pady=10,ipady=5) # padx=10, pady=10,
        self.numberChosen=ttk.Combobox(self, width=10,font=('微软雅黑', 10))
        self.numberChosen.grid(row=0, column=1,pady=10,ipady=5)
        self.numberChosen['values'] = ["皮夹", "来聚财", "生意人", "jenkins", "皮夹-电信", "来聚财-电信", "生意人-电信", "模拟银联支付"]
        self.numberChosen.current(0)
        Label(self, text="用户：").grid(row=1, column=0, ipadx=10,pady=10, ipady=5)
        self.usr =Entry(self, textvariable=self.var_usr,font=('微软雅黑', 10), width=12)
        self.usr.grid(row=1, column=1, pady=10, ipady=5)
        Label(self, text="密码：").grid(row=2, column=0, ipady=5)
        self.pwd=Entry(self, textvariable=self.var_pwd,font=('微软雅黑', 10), width=12)
        self.pwd.grid(row=2, column=1, pady=10,ipady=5)
        Button(self, text="登录", width=8, command=self.button1).grid(row=4, column=1,sticky=W)
    def huoqu(self):
        excel = xlrd.open_workbook(u'D:\zidonghua\常用网站记录.xls')
        nums = excel.sheet_by_index(0)
        row = nums.nrows
        for i in range(1, row):
            if self.wangzhan == nums.cell(i, 0).value:
                self.urll = nums.cell(i, 1).value
                usernamel = nums.cell(i, 2).value
                passwordl = nums.cell(i, 3).value
                if type(passwordl) == float:
                    passwordl = int(nums.cell(i, 3).value)
                else:
                    passwordl = nums.cell(i, 3).value
                break
        self.url = self.urll
        if self.var_usr.get() == '' or self.var_pwd.get() == '':
            username = usernamel
            password = passwordl
        else:
            username = self.var_usr.get()
            password = self.var_pwd.get()
        print(self.url,usernamel, passwordl)
        return self.url, username, password
    def button1(self):
        self.wangzhan = self.numberChosen.get()
        url,username, password = self.huoqu()
        self.usr.delete('0', "end")
        self.pwd.delete('0', "end")
        self.usr.insert('0', username)
        self.pwd.insert('0', password)
        sleep(1)
        driver = webdriver.Chrome()
        driver.maximize_window()
        if self.wangzhan == "来聚财":
            driver.get(url)
            driver.find_element_by_id("uname").send_keys(username)
            driver.find_element_by_id("pword").send_keys(password)
            driver.find_element_by_id("btn_login").click()
        elif self.wangzhan == "jenkins":
            driver.get(url)
            driver.find_element_by_id("j_username").send_keys(username)
            driver.find_element_by_name("j_password").send_keys(password)
            driver.find_element_by_id("yui-gen1-button").click()
        elif self.wangzhan == "皮夹":
            driver.get(url)
            driver.find_element_by_id("uname").send_keys(username)
            driver.find_element_by_id("pword").send_keys(password)
            driver.find_element_by_id("btn_login").click()
        elif self.wangzhan == "模拟银联支付":
            driver.get(url)
            driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[1]/div/div[2]/ul/li[1]/a').click()
        elif self.wangzhan == "皮夹-电信":
            driver.get(url)
            driver.find_element_by_id("uname").send_keys(username)
            driver.find_element_by_id("pword").send_keys(password)
            driver.find_element_by_id("btn_login").click()
        elif self.wangzhan == "来聚财-电信":
            driver.get(url)
            driver.find_element_by_id("uname").send_keys(username)
            driver.find_element_by_id("pword").send_keys(password)
            driver.find_element_by_id("btn_login").click()
        elif self.wangzhan == "生意人-电信":
            driver.get(url)
            driver.find_element_by_id("uname").send_keys(username)
            driver.find_element_by_id("pword").send_keys(password)
            driver.find_element_by_id("btn_login").click()
        else:
            driver.get(url)
            driver.find_element_by_id("uname").send_keys(username)
            driver.find_element_by_id("pword").send_keys(password)
            driver.find_element_by_id("btn_login").click()
class QueryFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()
    def button1(self):
        num = self.listb.size()
        result = []
        for i in range(0, num):
            if self.listb.selection_includes(i) == True:
                result.append(self.listb.get(i))
        driver = webdriver.Chrome()
        driver.get("http://192.168.55.10:8080/jenkins/login?from=%2Fjenkins%2F")
        driver.maximize_window()
        driver.find_element_by_id("j_username").send_keys('caiyong')
        driver.find_element_by_name("j_password").send_keys('Qwaszx12')
        driver.find_element_by_id("yui-gen1-button").click()
        sleep(1)
        for i in result:
            driver.find_element_by_xpath('//*[@title="Schedule a Build for %s"]' % i).click()
            sleep(1)
    def createPage(self):
        li = ['aus-bank', 'aus-nk-pjcore', 'aus-unionpay', 'aus-nk-bank', 'aus-merchant', 'aus-hcapp', \
              'aus-web', 'aus-wechat', 'aus-wechat-mp', 'boc-clear', 'aus-qrcode']
        self.listb=Listbox(self, width=100,height=230,selectmode=MULTIPLE)
        self.listb.grid(row=1, column=1,sticky=E+W, pady=5,ipady=70, ipadx=80)
        Button(self, text="构建", width=8, command=self.button1).grid(row=2,column=1,stick=W+E, pady=10)
        self.yscrollbar = tk.Scrollbar(self.listb, command=self.listb.yview)
        # self.yscrollbar.grid(row=1, column=2, sticky=N+S+W,pady=70, padx=60)  #
        self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listb.config(yscrollcommand=self.yscrollbar.set)
        self.label = Label(self, text='选择系统')
        self.label.grid(row=0, column=1, stick=W+E,pady=5)
        self.photo = PhotoImage(file='E:/python-jiaoben/tupian/11.gif')
        self.label = Label(self,compound = 'left',image=self.photo,width = 140, height =20)
        self.label.image=self.photo
        self.label.grid(row=1, column=0, sticky=W+E+N+S,ipady=10, ipadx=10,pady=5)
        self.photo = PhotoImage(file='E:/python-jiaoben/tupian/12.gif')
        self.label = Label(self, compound='right', image=self.photo, width=140, height=20)
        self.label.image = self.photo
        self.label.grid(row=1, column=2,  sticky=W+E+N+S,ipady=10, ipadx=10,pady=5)
        for item in li:
           self.listb.insert(0, item)
class dingcanFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()
    def createPage(self):
        Label(self, text="订餐人：").grid(row=0,column=1,sticky=W)
        """设置参数输入框"""
        self.datain = scrolledtext.ScrolledText(self, font=('微软雅黑', 10),width=40, height=8,  wrap=WORD)  #width=40, height=8,
        self.datain.grid(row=1, column=1, sticky=W)
        Label(self, text="请输入订餐人姓名，不同姓名以/隔开，例如张三/李四").grid(row=2,column=1,pady=10)
        '''设置按钮'''
        Button(self, text="订餐", width=8, command=self.button2).grid(row=1,column=2,padx=1,pady=1)   #sticky=W+E+N+S
        Button(self, text="清空", width=8, command=self.button1).grid(row=1,column=3,padx=5,pady=1)
    def button1(self):
        self.datain.delete("0.0", "end")
    def button2(self):
        self.datain.delete("0.0", "end")
class jiekouFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.var_url = StringVar()
        self.number = StringVar()
        self.createPage()
    def createPage(self):
        Label(self, text="URL：").grid(row=0, column=0,pady=5,sticky=W)
        Label(self, text="方式：").grid(row=0, column=2,pady=5)
        # numberChosen = ttk.Combobox(jiemian,width=10,textvariable=name).place(x=890, y=20)
        # numberChosen.append("post")
        Label(self, text="入参").grid(row=1, column=1, stick=W+E,pady=5)
        Label(self, text="出参").grid(row=1, column=3, stick=W+E,pady=5)
        '''设置文本框'''
        self.url = Entry(self, textvariable=self.var_url, font=('微软雅黑', 10),width=40)
        self.url.grid(row=0, column=1,stick=W)
        """设置请求方式下拉框"""
        self.numberChosen = ttk.Combobox(self, width=12, font=('微软雅黑', 10), textvariable=self.number)
        self.numberChosen['values'] = ("post", "get", "put", "delete")  # 设置下拉列表的值
        self.numberChosen.grid(row=0, column=3,pady=5,stick=W)  # 设置其在界面中出现的位置  column代表列   row 代表行
        self.numberChosen.current(0)
        """设置参数输入框"""
        self.datain = scrolledtext.ScrolledText(self, font=('微软雅黑', 10), wrap=WORD,width=40)
        self.datain.grid(row=2, column=1, rowspan=3,stick=W+E)   #  columnspan 占即列  rowspan  占几行
        self.dataout = scrolledtext.ScrolledText(self, font=('微软雅黑', 10), wrap=WORD,width=40)   #,width=30, height=30
        self.dataout.grid(row=2, column=3,rowspan=3, stick=W+E,padx=25)
        '''设置按钮'''
        Button(self, text="提交", width=8,command=self.button1).place(x=380, y=130)
        Button(self, text="清空出参", width=8,command=self.button2).place(x=380, y=190) #stick=N+S 上下排列中居中，stick=W+E 左右排列中居中
        Button(self, text="清空入参", width=8,command=self.button3).place(x=380, y=252)
        Button(self, text="格式化", width=8,command=self.button4).place(x=490, y=530)
        Label(self,text="接口").grid(row=6, column=0,padx=5,pady=10,stick=W)
    def renwu001(self):
        """根据入参获取出参"""
        data = self.datain.get("0.0", "end").strip()
        if data == "":
            """入参为空"""
            return self.renwu004()
        elif data != "":
            """入参不为空"""
            print(self.renwu003)
            return self.renwu003()
            # print(m.url)
            # print(data001)
    def renwu002(self):
        """出参展示在文本框"""
        self.dataout.insert("0.0", self.renwu001())
    def renwu003(self):
        """输出数据能够直接格式化"""
        self.data001 = eval(self.datain.get("0.0", "end").strip())  # 将str类型字符串字典化eval()
        # print(self.data001)
        if self.numberChosen.get() == "post":
            self.m = requests.post(url=self.url.get(), data=self.data001)
            # print(self.m.status_code)
            if self.m.status_code==404:
                message = {'msg': "请检查url地址", 'msg_code': "404"}
                json_str=json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
            else:
                json_str = json.dumps(eval(self.m.text), sort_keys=True, indent=2, ensure_ascii=False)
        elif self.numberChosen.get() == "get":
            self.m = requests.get(url=self.url.get(), data=self.data001)
            # print(self.m.status_code)
            if self.m.status_code==404:
                message = {'msg': "请检查url地址", 'msg_code': "404"}
                json_str=json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
            else:
                json_str = json.dumps(eval(self.m.text), sort_keys=True, indent=2, ensure_ascii=False)
        elif self.numberChosen.get() == "put":
            self.m = requests.put(url=self.url.get(), data=self.data001)
            if self.m.status_code==404:
                message = {'msg': "请检查url地址", 'msg_code': "404"}
                json_str=json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
            else:
                json_str = json.dumps(eval(self.m.text), sort_keys=True, indent=2, ensure_ascii=False)
        elif self.numberChosen.get() == "delete":
            self.m = requests.put(url=self.url.get(), data=self.data001)
            if self.m.status_code==404:
                message = {'msg': "请检查url地址", 'msg_code': "404"}
                json_str=json.dumps(message, sort_keys=True, indent=2, ensure_ascii=False)
            else:
                json_str = json.dumps(eval(self.m.text), sort_keys=True, indent=2, ensure_ascii=False)

        else:
            json_str = "很明显有问题，没选方式"
        return json_str
    def renwu004(self):
        """输出数据不能直接格式化"""
        self.m = requests.post(url=self.url.get(), data=self.datain.get("0.0", "end").strip())
        self.jsonnum = self.m.text.replace("null", '"null"').replace("true", '"true"').replace("false", '"false"')
        if self.numberChosen.get() == "post":
            try:
                json_str = json.dumps(eval(self.jsonnum), sort_keys=True, indent=2, ensure_ascii=False)
            except:
                json_str = self.jsonnum
        elif self.numberChosen.get() == "get":
            try:
                json_str = json.dumps(eval(self.jsonnum), sort_keys=True, indent=2, ensure_ascii=False)
            except:
                json_str = self.jsonnum
        elif self.numberChosen.get() == "put":
            try:
                json_str = json.dumps(eval(self.jsonnum), sort_keys=True, indent=2, ensure_ascii=False)
            except:
                json_str = self.jsonnum
        elif self.numberChosen.get() == "delete":
            try:
                json_str = json.dumps(eval(self.jsonnum), sort_keys=True, indent=2, ensure_ascii=False)
            except:
                json_str = self.jsonnum
        else:
            json_str = "很明显有问题，没选方式"
        return json_str
    def button1(self):
        self.dataout.delete("0.0", "end")
        self.renwu001()
        self.renwu002()
    def button2(self):
        self.dataout.delete("0.0", "end")
    def button3(self):
        self.datain.delete("0.0", "end")
    def button4(self):
        self.data002 = self.dataout.get("0.0", "end").strip()
        self.data003 = self.data002.replace("null", '"null"').replace("true", '"true"').replace("false", '"false"')
        self.json_str4 = json.dumps(eval(self.data003), sort_keys=True, indent=2, ensure_ascii=False)
        self.dataout.delete("0.0", "end")
        self.dataout.insert("0.0", self.json_str4)
class EWMFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()
    def createPage(self):
        Label(self, text="输入：").grid(row=0, column=0, stick=E, pady=5)
        self.url = Entry(self, font=('微软雅黑', 10), width=40)  # ,width=40
        self.url.grid(row=0, column=1, stick=E, pady=10, padx=5)
        self.label_img = Label(self, text="此处生成二维码")  # ,image=button()  ,image=path ,labelanchor=NW
        self.label_img.grid(row=2, column=1, stick=E + W, pady=10)  # , ipady=20, ipadx=20  row=3, column=1
        Button(self, text="生成二维码", width=28, command=self.button).grid(row=1, column=1, stick=E + W, pady=10)
    def button(self):
        # img, path, label = None, None, None
        global img, path, label
        self.img = qrcode.make(self.url.get())
        self.img.save("tupian.gif")
        self.path = PhotoImage(file='tupian.gif')
        self.label = Label(self, image=self.path, width=340, height=340)  # ,width=340,height=340
        self.label.grid(row=3, column=1, stick=E + W, pady=10, ipady=10, ipadx=10)


# login(jiemian)
mainpage(jiemian)
jiemian.mainloop()
