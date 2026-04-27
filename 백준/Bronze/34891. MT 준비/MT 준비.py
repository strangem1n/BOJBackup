import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = n // m
if n % m > 0:
    ans += 1
print(ans)