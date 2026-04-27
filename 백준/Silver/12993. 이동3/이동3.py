import sys
from itertools import combinations

def solve(a, b):
    c = a + b
    if c == 0:
        return 1
    arr = []
    k = 0
    while c > 0:
        i = 3 ** k
        c -= i
        arr.append(i)
        k += 1
        if c == 0:
            m = min(a, b)
            for j in range(len(arr)+1):
                for s in combinations(arr, j):
                    if m == sum(s):
                        return 1
    return 0

x, y = map(int, sys.stdin.readline().split())
print(solve(x, y))
