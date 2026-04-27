import sys
from collections import defaultdict
input = sys.stdin.readline

a, b = map(int, input().split())
r = int(input())
flower = defaultdict(bool)
flower[(a, b)] = True

cnt = 0
while True:
    cnt += 1
    if a + b + 2 < r:
        a += 1
        b += 1
    else:
        a //= 2
        b //= 2
    if flower[(a, b)]:
        break
    else:
        flower[(a, b)] = True
print(cnt)