import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    if arr[i] == 0:
        continue
    arr[i] += arr[i-1]
print(sum(arr))
