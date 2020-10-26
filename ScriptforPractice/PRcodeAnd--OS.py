# 练习双色图脚本
# tell():返回当前帧数
# save():保存帧图
# seek():寻找指定帧
# 对其进行修改,原本是自己创建输出文件夹才能完成,现在补充输出创建过程

from PIL import Image
import os


def main(gif):
    png_file = 'S:\\Kali\\Misc\\g29\\'
    png_path = png_file+'pngtest\\'
    exist = os.path.exists(png_path)
    if not exist:
        os.mkdir(png_path)
        print(png_path+" 目录不存在,并已创建")
    else:
        print(" 文件目录存在 ")
    im = Image.open(png_file+gif)
    try:
        while True:
            current = im.tell()
            im.save(png_path+str(current+1)+'.png')
            im.seek(current+1)
    except:
        pass
    print('分离完成')


if __name__ == '__main__':
    gif = 'out.gif'
    main(gif)


'''小结：

此处拓展了文件目录创建的过程
import os    导入os模块,os是python标准库中用于访问操作系统功能的模块
系统操作：
    os.sep  系统路径的分隔符
    os.name 正在使用的工作平台
    os.getenv  读取环境变量
    os.getcwd() 获取当前的路径
目录操作-增删改查：
    os.listdir(): 返回指定目录下的所有文件和目录名 ，注返回的是多个数据
    os.mkdir():创建一个目录。只创建一个目录文件
    os.rmdir():删除一个空目录。若目录中有文件则无法删除
    os.makedirs(dirname):生成多层递归目录。如果目录全部存在，否则失败
    os.removedirs(dirname):删除多层递归的空目录，若目录中有文件则失败
    os.chdir():改变当前目录，到指定目录中
    os.rename():重命名目录名和文件名。若重命名后的文件重复则失败
判断：
    os.path.exists(path):判断文件或者目录是否存在，是True,否False
    os.path.isfile(path):判断是否为文件。是返回True,否返回False
    os.path.isdir(path):判断是否为目录。是返回True,否返回False
Path模块：
    os.path.basename(path):返回文件名
    os.path.dirname(path):返回文件路径
    os.path.getsize(path):获得文件大小，如果name是目录返回OL;
    os.path.abspath(name):获取绝对路径
    os.path.join(path.name):连接目录与文件名或目录  
'''