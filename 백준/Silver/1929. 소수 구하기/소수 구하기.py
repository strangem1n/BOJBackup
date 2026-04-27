import math
m, n = map(int, input().split())
if m == 1:
    m += 1
for i in range(m, n+1):
    check = True
    root = int(math.sqrt(i))
    for j in range(2, root+2):
        if i == 2:
            break
        elif i % j == 0:
            check = False
            break
    if check is True:
        print(i)