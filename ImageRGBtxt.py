# 用于RGB模式下,知道3*8位像素值的文本，从而还原图像
# 如: 255,255,255
from PIL import Image  # 调用库，包含图像类

img = Image.new('RGB', (503, 122), "black")
# mode:RGB(3*8像素，真彩) size:元组（width, height）单位像素 color:通道颜色默认全黑
x = 503
y = 122
f = open('S:\\Kali\\Misc\\g29.txt', 'r')    # 第一个存放路径名,实验文档g29.txt
pix =[]     # 预存放文本内数值
for i in range(61366):      # 循环文本行数
    a = f.readline()        # 读取每一行字符串并赋值给a ,注readline()会读取换行符
    a = a.replace('\n', '')  # 将换行符替换空值
    pix.append(a)   # 将每一行的数值除去换行符，拼接到pix列表中

im = []     # 定义一个im
for i in range(len(pix)):   # 循环pix的列表内容
    im.append(pix[i].split(','))    # 将pix中的字符串通过','进行分隔三个数组并拼接到im

for i in range(x):  # 循环宽度
    for j in range(y):  # 循环高度
        pix = (int(im[i*122+j][0]), int(im[i*122+j][1]), int(im[i*122+j][2]))
        # 按上述算法将im每个值写进 一个元组包含三个数据
        img.putpixel((i, j), pix)
        # 在像素i,j 位置 ,写入像素值--至此完成图像的操作
img.show()     # 显示图像

