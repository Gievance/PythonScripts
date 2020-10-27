# 用于分离不同通道下的图片

from PIL import Image

path = 'S:\\Kali\\Misc\\hardcodewatermark01\\'
p = Image.open(path + "sub.bmp")
w, h = p.size

for n in range(3):
    np = Image.new("RGB", (w, h), (255, 255, 255))
    if n == 0:
        for i in range(h):
            for j in range(w):
                if p.getpixel((j, i))[0] > 240:
                    np.putpixel((j, i), (240, 0, p.getpixel((j, i))[2]))
        np.save(path + 't2.png')
        break
    if n == 1:

        for i in range(h):
            for j in range(w):
                if p.getpixel((j, i))[1] > 240:
                    np.putpixel((j, i), p.getpixel((j, i)))
        np.save(path + 'g2.png')
    if n == 2:

        for i in range(h):
            for j in range(w):
                if p.getpixel((j, i))[2] > 240:
                    np.putpixel((j, i), p.getpixel((j, i)))
        np.save(path + 'b2.png')

print('完成')
