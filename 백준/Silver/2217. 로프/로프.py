import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
ans = 0
for i in range(n):
    a = arr[i] * (i+1)
    if ans < a:
        ans = a
print(ans)
