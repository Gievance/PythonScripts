# 然后读取每个png中的对应点的信息，并按照8bit转换为ascii
from PIL import Image


def main():
    png_path = 'S:/Kali/Misc/g29/output/'
    ret = ''
    for i in range(24):
        line = ''
        for j in range(24):
            img = Image.open(png_path + str(i * 24 + j + 1) + '.png')
            img = img.convert("RGB")    # 将图片转成RBG 是load返回元组
            img_arr = img.load()        # load返回int

            x = j*10+5          # x 是 j
            y = i*10+5          # y 是 i
            r, g, b = p = img_arr[x, y]       # 区别：二维数组的访问是[x, y] 不是[x][y]
            if g == 255:
                line += '0'
            if r == 255 and b == 255:
                line += '1'
            if len(line) == 8:
                ret += chr(int(line, 2))
                line = ''
    print(ret)
    #DES加密：flag{2ce3b416457d4380dc9a6149858f71db}


if __name__ == '__main__':
    main()