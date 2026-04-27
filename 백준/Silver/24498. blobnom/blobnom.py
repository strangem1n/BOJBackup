import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = max(arr[0], arr[-1])
for i in range(1, n-1):
    a = arr[i] + min(arr[i-1], arr[i+1])
    if ans < a:
        ans = a
print(ans)
