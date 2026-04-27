import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_diff = float('inf')
cnt = 0
for i in range(1, n):
    diff = arr[i] - arr[i-1]
    if min_diff > diff:
        min_diff = diff
        cnt = 1
    elif min_diff == diff:
        cnt += 1

print(min_diff, cnt)