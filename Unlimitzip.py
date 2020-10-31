#  获取zip中的zip...
import zipfile
import re

filepath = 'Zip/46783.zip'
while True:
    if filepath != 'Zip/73168.zip':
        zip = zipfile.ZipFile(filepath)
        res = re.search('[0-9]*', zip.namelist()[0])
        passwd = res.group()
        try:
             zip.extractall('Zip/', pwd=passwd.encode('utf-8'))
        except:
            print(filepath)
            pass
        filepath = 'Zip/' + zip.namelist()[0]
        print(filepath)

    else:
        print("解压完成")
#Zip/12475.zip
# Zip/mess.wav
'''

在 Python 中，有 2 种常用的字符串类型，分别为 str 和 bytes 类型，
其中 str 用来表示 Unicode 字符，bytes 用来表示二进制数据。
str 类型和 bytes 类型之间就需要使用 encode() 和 decode() 方法进行转换。 
encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，
这个过程也称为“编码”。
encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，
这个过程也称为“编码”。
'''