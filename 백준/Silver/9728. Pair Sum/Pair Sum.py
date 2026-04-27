import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    for a in arr:
        want = m - a
        if want <= a:
            break
        idx = bisect_left(arr, want)
        if idx < n and arr[idx] == want:
            result += 1
    print(f'Case #{tc}: {result}')