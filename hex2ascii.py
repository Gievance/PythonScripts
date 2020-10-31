"""-------------------------

本文档是将一串类似16进制的字符转成ascii码
ascii码有128个字符，一个字符=一个字节=由两个16进制表示
"""
import binascii

s = 'd4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c' \
    '3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd'
num = []
for i in range(0, len(s), 2):
    num.append(s[i:i + 2])
# print(num)
flag = ''
for j in num:
    flag += chr(int(j, 16)-128)
print(flag)

'''小结：

这里有个失误点：
int('0x0a', 16) =10   参数意义是 0x0a是16进制，请转化成10进制
'''