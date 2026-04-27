import sys
from collections import defaultdict
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
d = defaultdict(int)
for i in a:
    d[i] += 1
for i in b:
    d[i] -= 1
print(sum(map(abs, d.values())))