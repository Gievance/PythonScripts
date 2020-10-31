# g44.txt

Path = 'Txt/g44.txt'
flag = ''
with open(Path, 'r') as infile:
    file = infile.read()
    # print(file)
    # print(len(file))
    for i in range(0, len(file), 8):
        temp = file[i:i+8]
        tmp = ''
        for j in range(len(temp)):
            if temp[j] == '1':
                tmp += '0'
            else:
                tmp += '1'
        # print(tmp)
        flag += chr(int(tmp, 2))
print(flag) # Heisenberg