import base64


def Toten(value):
    sum = 0
    for k in range(len(value)):  # 原理，多进制变十进制，每一位的x*y^(n-1)的和。
        count = int(value[k]) * (8 ** (len(value) - 1 - k))
        sum += count
    return sum


if __name__ == '__main__':
    # 实现八进制转16进制
    with open(r'S:\Kali\Misc\隐藏的信息\message.txt', 'r') as path:
        m = path.read().strip().split(' ')
    res = ''
    for i in m:
        res += chr(Toten(i))
    print(base64.b64decode(res))