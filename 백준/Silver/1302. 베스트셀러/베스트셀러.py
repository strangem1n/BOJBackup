import sys
from collections import defaultdict
input = sys.stdin.readline

sell = defaultdict(int)
n = int(input())
for _ in range(n):
    sell[input().rstrip()] += 1
score = sorted(sell.items(), key=lambda x: (-x[1], x[0]))
print(score[0][0])
