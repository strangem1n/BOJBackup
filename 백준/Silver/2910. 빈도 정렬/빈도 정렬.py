import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
d = defaultdict(int)
arr = map(int, input().split())
for a in arr:
    d[a] += 1
for i, j in sorted(d.items(), key=lambda x: -x[1]):
    print(f"{i} "*j, end="")
