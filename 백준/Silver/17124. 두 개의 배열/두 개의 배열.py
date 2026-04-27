import sys
from bisect import bisect_left
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(map(int, input().split()))
    res = 0
    for ai in a:
        idx = bisect_left(b, ai)
        if idx == m:
            res += b[idx-1]
        elif idx == 0:
            res += b[0]
        else:
            left, right = b[idx-1], b[idx]
            if abs(ai - left) <= abs(ai - right):
                res += left
            else:
                res += right
    print(res)