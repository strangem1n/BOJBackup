import sys
input = sys.stdin.readline

n, k = map(int, input().split())
g = (k*(k+1)//2)
if n < g:
    print(-1)
else:
    arr = [i for i in range(1, k+1)]
    left = n - g
    idx = 0
    while left > 0:
        left -= 1
        idx = (idx + 1) % k
        arr[-idx] += 1
    print(arr[-1] - arr[0])