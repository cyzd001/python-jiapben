import os

print(os.path.exists('test002.py'))
print(os.path.exists(u'总控登录.py'))

"""使用os.access()方法判断文件是否可进行读写操作。语法：
os.access(path, mode)
path为文件路径，mode为操作模式，有这么几种:
os.F_OK: 检查文件是否存在;
os.R_OK: 检查文件是否可读;
os.W_OK: 检查文件是否可以写入;
os.X_OK: 检查文件是否可以执行"""