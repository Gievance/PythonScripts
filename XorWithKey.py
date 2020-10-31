# 参考异或加密原理

key = 'GoodLuckToYou'
flag = ''

with open('S:\\Kali\\Misc\\g40', 'rb') as file:
    con = file.read()
    for i in range(len(con)):
        flag += chr(con[i] ^ ord(key[i % 13]))  # 以及是字节类型了，不需要对con[i]+个ord
print(flag)


print('完成')
