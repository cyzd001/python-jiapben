from selenium import webdriver
from time import sleep
from PIL import Image, ImageEnhance
from pytesseract import *


im=Image.open('getVerifyCode.png')
im = im.convert('L')#图像加强，二值化
sharpness =ImageEnhance.Contrast(im)#对比度增强
sharp_img = sharpness.enhance(2.0)
sharp_img.save("newVerifyCode.png")
newVerify = Image.open('newVerifyCode.png')
# 使用image_to_string识别验证码
text=image_to_string(newVerify).replace(' ', '') #使用image_to_string识别验证码
sleep(1)
print(text)

for i in range(1,10):
    im = Image.open('getVerifyCode.png')
    im = im.convert('L')  # 图像加强，二值化
    sharpness = ImageEnhance.Contrast(im)  # 对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save("newVerifyCode.png")
    newVerify = Image.open('newVerifyCode.png')
    # 使用image_to_string识别验证码
    text = image_to_string(newVerify).replace(' ', '')  # 使用image_to_string识别验证码
    sleep(1)
    print(text,end = "")