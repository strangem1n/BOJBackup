import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
for a in arr:
    ans += 1
    a -= b
    if a <= 0:
        continue
    ans += a // c
    if a % c > 0:
        ans += 1
print(ans)
