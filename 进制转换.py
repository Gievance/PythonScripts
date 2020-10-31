'''目前实现不同进制向十进制的转换'''
def ToTen(content, jz):
    sum = 0
    for i in range(len(content)):
        count = int(content[i]) * (int(jz) ** (len(content) - 1 - i))
        sum += count
    return int(sum)


if __name__ == '__main__':
    print('''
--------输入内容--------
(目前只有 转换十进制数)
''')
    content = input("输入内容=")
    print('''-------输入进制--------''')
    jz = input('输入进制=')
    print(ToTen(content, jz))
