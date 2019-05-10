import pytesseract
from PIL import Image

newVerify = Image.open('newVerifyCode.png')
print(type(newVerify))
print(newVerify)
# 使用image_to_string识别验证码
text=pytesseract.image_to_string(newVerify).replace(' ', '')  #使用image_to_string识别验证码
#text1 = image_to_string('newVerifyCode.png').strip()
print(text)