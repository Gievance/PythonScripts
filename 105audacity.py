# 步长的含义：下一索引位置 = 当前索引位置 + 步长


def main(string):
    ret = ''
    if len(string) % 8 == 0:
        for i in range(0, len(string), 8):      # 步长为8，代表跳过8个字符，符合ascii 8
            ret += chr(int(string[i:i + 8], 2))

    if len(string) % 7 == 0:
        for i in range(0, len(string), 7):      # 步长为7，代表跳过7个字符，符合ascii 7
            ret += chr(int('0' + string[i:i + 7], 2))
    else:
        print("不能被7和8整除")

    print(ret)


if __name__ == '__main__':
    with open('S:\\Kali\\Misc\\g32\\音频开头.txt') as obj:
        txt = obj.read()
    print(txt)
    main(txt)
    # 参考如下：利用步长完成对ascii 7\8的划分
    # flag = txt
    # for i in range(0, len(txt), 7):
    #     c_flag = txt[i:i + 7]
    #     print(c_flag)
    #     flag += chr(int(c_flag, 2))
    # print(flag)
