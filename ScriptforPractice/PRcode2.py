# 帧分离操作完成，现进行像素采取

from PIL import Image

def main():
    png_path = 'S:\\Kali\\Misc\\g29\\pngtest\\'
    ret = ''
    for i in range(24):
        line = ''
        for j in range(24):
            img = Image.open(png_path+str(i*24+j+1)+'.png')
            img = img.convert("RGB")
            pix = img.load()
            x = j*10+5
            y = i*10+5
            r, g, b = pix[x, y]
            if g == 255:
                line += '0'
            if r == 255 and b == 255:
                line += '1'
            if len(line) == 8:
                ret += chr(int(line, 2))  # 这地方强转一定是2进制的形式
                line = ''
    print(ret)


if __name__ == '__main__':
    main()

# 结果o8DlxK+H8wsiXe/ERFpAMaBPiIcj1sHyGOMmQDkK+uXsVZgre5DSXw==hhhhhhhhhhhhhhhh  结合key =DES 加密