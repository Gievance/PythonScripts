with open('S:\\Kali\\Misc\\奇怪的TTL字段\\ttl.txt') as ttl:
    lines = ttl.readlines()     # 返回一个列表，其元素由每一行组成

num = []
for line in lines:
    num.append(int(line.replace('TTL=', '')))       # 将TTL对应的数字存放在列表汇总


bnum = ''
for i in range(len(num)):       #将num中的数字的高二位保存
    if num[i] == 127:
        bnum += '01'
    elif num[i] == 191:
        bnum += '10'
    elif num[i] == 63:
        bnum += '00'
    elif num[i] == 255:
        bnum += '11'
    else:
        print("错误")

# 转换成字符
ret = ''
for j in range(0, len(bnum), 8):
    ret += chr(int(bnum[j:j+8], 2))

# 导出文件
with open('S:\\Kali\\Misc\\奇怪的TTL字段\\f2.txt', 'w') as out:
    out.write(ret)
print("完成")