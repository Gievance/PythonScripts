# coding = utf-8
# 此脚本使用了bitstring模块,旨在帮助 尽可能简单自然地创建和分析二进制数据
# 注：好用
# 借鉴了G45.py
# 弥补bitstring模块
from PIL import Image
import bitstring

with Image.open('Images/g45.png') as img:  # 此处丢失Image
    width, height = img.size
    pix = img.load()
    bin_res = ''
    for h in range(height):
        for w in range(width):
            if pix[w, h][0] == 255:
                bin_res += '1'
            else:
                bin_res += '0'
    with open('Images/g45flag.png', 'wb') as out:
        out.write(bitstring.BitArray(bin=bin_res).bytes)    # 一定要有（bin=）标识bin_res是二进制
        print('完成')