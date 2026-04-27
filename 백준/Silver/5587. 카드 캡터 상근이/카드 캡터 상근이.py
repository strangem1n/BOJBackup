import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
card = defaultdict(int)
for _ in range(n):
    card[int(input())] = 1

sanggeun = geunsang = n
table = 0
while sanggeun > 0 and geunsang > 0:
    for i in range(table+1, 2*n+1):
        if card[i] == 1:
            card[i] = 2
            table = i
            sanggeun -= 1
            break
    else:
        table = 0

    if sanggeun == 0 or geunsang == 0:
        break

    for i in range(table+1, 2*n+1):
        if card[i] == 0:
            card[i] = 2
            table = i
            geunsang -= 1
            break
    else:
        table = 0

if sanggeun == 0:
    print(geunsang)
    print(0)
else:
    print(0)
    print(sanggeun)