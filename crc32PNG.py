# CRC32爆破出匹配的高度 WDCTF.png

import binascii
import struct

crc = 0x932F8A6B
file = open('S:\\Kali\\Misc\\WDCTF.png', 'rb').read()
for i in range(1024):
    data = file[12:16]+struct.pack('>i', i) + file[20:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc == crc32:
        print(i)
