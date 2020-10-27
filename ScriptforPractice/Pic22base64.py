# coding:utf8

import base64  # 导入base64模块
import os


def pictob64(path):  # 将图片转换成base64格式
    with open(path, 'rb') as pic:  # 以 读字节的方式打开图片
        b64 = base64.b64encode(pic.read())  # b64对图片字节进行加密, 返回加密后的字节值
        # print(str(b64, 'utf8'))
        # 验证后发现没有str(b64, 'utf8')也行
        # 其实不行,b64encode返回时字节值 b '****'
        # 加str(b64, 'utf8')会转成utf 则去掉了b.不然base64加密的值中前有b
        # print('--------------------------')
        # print(b64)
        with open("S:\\Kali\\Misc\\WDCTF\\_1.zip.extracted\\b64.txt", 'wt') as out:
            # print(str(b64))
            out.write(str(b64), 'utf8')


def b64topic(path):  # base64转图片
    with open(path, 'rb') as b64:
        pic = base64.b64decode(b64.read())
        with open('out.png', 'wb') as p:
            p.write(pic)


# 执行此脚本

print('''请输入：
          1-图片转base64
          2-base64 转图片（PNG格式)  
            
            ''')

c = eval(input())
if c == 1:
    print('请输入图片文件名+后缀')
    picfile = input("filename=")
    pictob64(picfile)
elif c == 2:
    print('请输入base64文件名+后缀')
    b64file = input("b64name=")
    b64topic(b64file)
else:
    print("您输入了个鬼？")
