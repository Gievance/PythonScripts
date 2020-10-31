# 对low.bmp图片进行奇偶二值化处理
from PIL import Image

with Image.open('Images/low.bmp') as img:
    pix = img.load()  # 加载图片信息到pix
    # 方法load()返回一个用于读取和修改像素的像素访问对象。这个访问对象像一个二维队列
    img2 = Image.new('L', img.size, 255)  # L	8位像素，黑白 0为黑，255为白
    out = img2.load()  # 创建一个新图片out
    w, h = img.size  # 获取长宽
    for i in range(h):
        for j in range(w):
            if pix[j, i] & 1 == 0:
                out[j, i] = 0
            else:
                out[j, i] = 255
    img2.show()

'''小结：用load的方法修改像素很

load()只是返回一个对像素操作的对象，读取图片属性什么的还是依靠图片图像
new(mode, size, color )注意new 方法的元素
关于LSB隐写的判断
@@当你用StegSolve切换通道时，注意到red plane0、green plane0、blue plane0相同时可以判断为LSB隐写
'''