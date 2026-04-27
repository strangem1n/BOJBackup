import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, m):
    arr[i] += arr[i-1]
for _ in range(n):
    idx = bisect_left(arr, int(input())) + 1
    if idx > m:
        print("Go away!")
    else:
        print(idx)
