'''已知ID为0x8893CA58的温度传感器的未解码报文为：3EAAAAA56A69AA55A95995A569AA95565556

此时有另一个相同型号的传感器，其未解码报文为：3EAAAAA56A69AA556A965A5999596AA95656
请解出其ID，提交格式为flag{xxx}
'''


def Machest(code):
    bin2 = bin(code)[2:]
    res = ''
    for i in range(int(len(bin2) / 2)):
        a = bin2[i * 2:i * 2 + 2]
        if a != '10' and a != '01':
            continue
        if a == '10':
            res += '1'
        else:
            res += '0'
    print(hex(int(res, 2)).upper())


def CManchest(code):
    bin2 = bin(code)[2:]
    # print(bin2)   # 带有0b
    res = ''
    for i in range(int(len(bin2) / 2)):  # 两个一组，则长度为一半
        tmp1 = bin2[i * 2:i * 2 + 2]
        tmp2 = bin2[i * 2 + 2:i * 2 + 4]
        if tmp1 != '10' and tmp1 != '01':
            continue
        if tmp2 != '10' and tmp2 != '01':
            continue
        if tmp1 != tmp2:
            res += '1'
        else:
            res += '0'
    print(hex(int(res, 2)).upper())


if __name__ == '__main__':
    a = 0x3EAAAAA56A69AA55A95995A569AA95565556
    b = 0x3EAAAAA56A69AA556A965A5999596AA95656
    id = 0x8893CA58
    print('--------CManchest-------------')
    CManchest(a)  # 0X24D 8893CA58 4181
    CManchest(b)  # 0X24D 8845ABF3 4119
    print('--------Manchest--------------')
    Machest(a)
    Machest(b)
