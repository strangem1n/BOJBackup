import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
for _ in range(m):
    order = input().rstrip()
    if order[0] == "3":
        a, i, j = map(int, order.split())
        print(bisect_right(arr, j)-bisect_left(arr, i))
    else:
        a, k = map(int, order.split())
        if a == 1:
            print(n-bisect_left(arr, k))
        else:
            print(n-bisect_right(arr, k))
