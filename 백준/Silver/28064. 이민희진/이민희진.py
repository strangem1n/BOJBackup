import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
names = [input().rstrip() for _ in range(n)]
c = combinations(names, 2)
cnt = 0
for ci in c:
    s, t = ci
    for idx in range(1, (min(len(s), len(t)))+1):
        if s[:idx] == t[-idx:]:
            cnt += 1
            break
        elif s[-idx:] == t[:idx]:
            cnt += 1
            break
print(cnt)