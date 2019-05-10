from tkinter import *
import qrcode
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import scrolledtext
import hashlib
import base64

def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y

jiemian = Tk()
jiemian.title("登录小助手")
a, b = jiemian_info()
jiemian.geometry("800x600+%d+%d" % (a, b))
text = scrolledtext.ScrolledText(jiemian,width=40)
text.grid(row=1, column=1, rowspan=10,stick=W,pady=10,padx=5)  #columnspan=1,
text1 = scrolledtext.ScrolledText(jiemian,width=40)
text1.grid(row=1, column=3, rowspan=10,stick=W,pady=10,padx=5)
def choosepic():
    path_=askopenfilename()
    # path.set(path_)
    with open(path_) as file1:
        file2 = file1.read().split()    #.split()
    text.insert("0.0", file2)
def baocun():
    path = asksaveasfilename()
    path.save()
def jiami():
    neirong = text.get("0.0", "end")
    print(neirong)
    hl = hashlib.md5(neirong.encode(encoding='UTF-8')).hexdigest().upper()  #upper() 字母转换为大写
    text1.delete("0.0", "end")
    text1.insert("0.0", hl)
def jiami001():
    neirong = text.get("0.0", "end")
    print(neirong)
    hl = base64.b64encode(neirong.encode(encoding='UTF-8'))
    text1.delete("0.0", "end")
    text1.insert("0.0", hl)
def jiami002():
    neirong = text.get("0.0", "end")
    print(neirong)
    hl = base64.b64decode(neirong.encode(encoding='UTF-8'))
    text1.delete("0.0", "end")
    text1.insert("0.0", hl)

Button(jiemian,text="打开",width=10,command=choosepic).grid(row=1, column=2,pady=5,padx=5)  #stick=E+W
Button(jiemian,text="保存",width=10,command=baocun).grid(row=2, column=2,pady=5,padx=5)  #stick=E+W
Button(jiemian,text="MD5加密",width=10,command=jiami).grid(row=3, column=2,pady=5,padx=5)  #stick=E+W
Button(jiemian,text="base64加密",width=10,command=jiami001).grid(row=4, column=2,pady=5,padx=5)  #stick=E+W
Button(jiemian,text="base64解密",width=10,command=jiami002).grid(row=5, column=2,pady=5,padx=5)  #stick=E+W
jiemian.mainloop()