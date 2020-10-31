import base64
# pthon3 默认采用Unicode编码
'''s1 = 'this is a test for base64'

tmp1 = base64.b64encode(s1.encode('utf-8')) # 未encode,则有报错,b64encode的参数为字节对象
print(tmp1)     # b'dGhpcyBpcyBhIHRlc3QgZm9yIGJhc2U2NA=='
print(tmp1.decode())    # dGhpcyBpcyBhIHRlc3QgZm9yIGJhc2U2NA==
print(tmp1.decode('utf-8'))     # dGhpcyBpcyBhIHRlc3QgZm9yIGJhc2U2NA==
print(tmp1.decode('latin'))     # dGhpcyBpcyBhIHRlc3QgZm9yIGJhc2U2NA==
res = base64.b64decode(tmp1)

res = base64.b64decode(tmp1.decode()) # 解码接收字符串或字节类型
print(res)  # b'this is a test for base64'
print(res.decode()) # this is a test for base64


print('----------------------------')
s2 = b'this is a byte test'
tmp2 = base64.b64encode(s2)
print(tmp2)     # 无报
print(tmp2.decode())'''
src = '19aaFYsQQKr+hVX6hl2smAUQ5a767TsULEUebWSajEo='
print(src.encode('utf-8'))
res = base64.b64decode(src)
print(res.decode('latin'))

src2 = '这是测试解码'
src2 = base64.b64encode(src2.encode('utf-8'))   # 转为bytes类型
res2 = base64.b64decode(src2).decode('utf-8')
print(res2)