import sys

u = sys.stdin.readline()
y = "YONSEI"
k = "KOREA"
yi = ki = 0
for i in u:
    if i == y[yi]:
        yi += 1
    if i == k[ki]:
        ki += 1
    if yi == 6:
        print(y)
        break
    if ki == 5:
        print(k)
        break