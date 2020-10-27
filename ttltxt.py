with open('S:\\Kali\\Misc\\奇怪的TTL字段\\ttl.txt') as ttl:
    lines = ttl.readlines()
    # print(lines)
num = []
for line in lines:
    num.append(int(line.replace('TTL=', '')))
# print(num)

res = ''
for i in range(len(lines)):
    tem = bin(num[i])[2:]
    tem = '0' * (8 - len(tem)) + tem
    res += tem[0:2]

res2 = ''
for j in range(0, len(res), 8):
    res2 += chr(int(res[j:j + 8], 2))
    with open('S:\\Kali\\Misc\\奇怪的TTL字段\\flag2.txt', 'w') as out:
        out.write(res2.rstrip())
print('完成')
