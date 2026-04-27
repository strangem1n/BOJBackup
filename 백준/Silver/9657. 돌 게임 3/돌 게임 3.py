import sys

n = int(sys.stdin.readline())
dp = [True] * n
if n > 1:
    dp[1] = False

for i in range(4, n):
    if dp[i-1] and dp[i-3] and dp[i-4]:
        dp[i] = False

if dp[-1]:
    print("SK")
else:
    print("CY")