from math import floor,sqrt
from string import printable
s = '153 33 113 45 118 185 228 27 33 51 252 236 90 252 160 252 33 27 85 252 176 33 106 139 228 101 252 33 179 176 33 106 252 236 123 160 68 62 33 99 236 79 123'
l = [int(i) for i in s.split()]

def get_poss_values(key,oup) :
    l = []
    for x in range(key+1):
        if chr(x) not in printable:
            continue
        am=(key+x)/2
        gm=sqrt(key*x)
        if (oup == floor(am+gm)%255):
            l.append(x)
    return l

for key in range(101*10,101*122+1):
    op = []
    ans = True
    for x in l:
        val = get_poss_values(key,x)
        if len(val) == 0:
            ans = False
            break
        else:
            op.append(val)
    if (ans):
        print(key,op)
        break

key = 10706//101
l = [[39, 73], [95], [67], [97], [110], [78], [48], [55], [95], [98], [51], [49], [105], [51], [74, 118], [51], [95], [55], [63, 104], [51], [121], [95], [66], [114], [48], [107], [51], [95], [42, 77], [121], [95], [66], [51], [49], [111], [74, 118], [101], [100], [95], [65], [49], [103], [111]]

ops = ['']
for i in l:
    ops2 = []
    for x in ops:
        for v in i:
            ops2.append(x+chr(v))
    ops = ops2
print(ops)