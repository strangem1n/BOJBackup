import sys
from itertools import combinations

arr = [int(sys.stdin.readline()) for _ in range(9)]
for a in combinations(arr, 7):
    if sum(a) == 100:
        print(*a, sep="\n")
        break
