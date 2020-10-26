string = "cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_" \
         "rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987" \
         "k5tfb_hjiouo087ptfcv}"
a = ''
for i in range(3, len(string), 5):       # range(start, stop, step)
    a += string[i]      # str没有append属性

print(a)

