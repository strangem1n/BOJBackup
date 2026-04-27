def chkdigits(num):
    if len(str(num)) == 1:
        num1 = 0
        num2 = str(num)
    elif len(str(num)) == 2:
        num1 = str(num)[0]
        num2 = str(num)[-1]
    return int(num1), int(num2)

def cycle(num):
    sumnum = num[0] + num[1]
    newnum = str(num[1]) + str(sumnum)[-1]
    return int(newnum)

import sys
n = int(sys.stdin.readline())
chknum = n
newnum = None
check = 0

while True:
    a = chkdigits(chknum)
    newnum = cycle(a)
    check += 1
    if n == newnum:
        break
    else:
        chknum = newnum
        continue

print(check)