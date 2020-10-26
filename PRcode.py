# gif 分离单帧--out.gif ：其为24*24像素点,每个像素点为10*10方格组成240*240像素

from PIL import Image  # 导入Image类


def main(gif):  # 定义main函数
    png_dir = 'S:\\Kali\\Misc\\g29\\'  # 定义帧输出路径
    img = Image.open(png_dir + gif)  # 打开out.gif文件
    try:
        while True:  # 循环保存帧
            current = img.tell()  # 获取当前帧数
            img.save(png_dir + 'output\\' + str(current + 1) + '.png')  # 保存帧
            # 注：没有output文件夹,所有无结果，创建该文件夹后，出现帧分离后的文件
            img.seek(current + 1)  # 获取下一帧
    except:
        pass  # 异常pass


'''if __name__ == '__main__':的运行原理

每个python模块（python文件，比如 test.py 和 import_test.py）都包含内置的变量 __name__，
当该模块被直接执行的时候，__name__ 等于文件名（包含后缀 .py ）；如果该模块 import 到其他模块中，
则该模块的 __name__ 等于模块名称（不包含后缀.py）。
而“__main__” 始终指向当前执行模块的名称（包含后缀.py）。进而当模块被直接执行时，__name__ == 'main' 结果为真。 
'''
if __name__ == '__main__':
    gif_file = 'out.gif'
    main(gif_file)
