import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [n] * (n+1)
dp[-1] = 0
for i in range(n-1, -1, -1):
    for j in range(arr[i], 0, -1):
        if i + j > n:
            continue
        dp[i] = min(dp[i], 1 + dp[i+j])
print(dp[0])
