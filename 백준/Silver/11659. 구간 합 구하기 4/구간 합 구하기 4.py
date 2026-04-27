import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for x in range(1, len(arr)):
    arr[x] += arr[x-1]
for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j-1] - arr[i-2] if i > 1 else arr[j-1])
