import base64

key = 'This is a test for Xor'
print('----------------------')
for i in range(len(key)):
    print(ord(key[i]))  # 很明显是十进制
print('----------------------')
for i in range(len(key)):
    print(chr(ord(key[i])))  # 很明显转换成字符
print('--------------------')
# for i in range(len(key)):
print(bin(0b00001111 ^ ord('s')))
print('---------------------------')
with open('S:\\Kali\\Misc\\g40', 'rb') as file:
    con = file.read()
    print(con)
    print('-----enumerate')
    for pos, c in enumerate(con):
        print('{0}:{1}'.format(pos, c))

s = 'd4'
s2 = 'A'
print(int(s, 16))
print(int(s2, 16))
# int() 是将字符转化成10进制，其字符进制由后面参数确定
strs = '19aaFYsQQKr+hVX6hl2smAUQ5a767TsULEUebWSajEo='
print(strs.encode())
res = base64.b64decode(strs.encode('latin'))
print(res)
print(res.decode('latin'))