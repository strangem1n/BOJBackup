import sys
from collections import defaultdict
input = sys.stdin.readline

cow_cnt = defaultdict(int)
n = int(input())
for _ in range(n):
    cow_group = list(input().split())
    cow_group.sort()
    cow_cnt[tuple(cow_group)] += 1
print(max(cow_cnt.values()))
