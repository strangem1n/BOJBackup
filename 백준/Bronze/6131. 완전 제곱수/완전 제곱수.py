import sys, math
n = int(sys.stdin.readline())

ans = 0
for i in range(1, n):
    a = math.sqrt(i**2 + n)
    if a == int(a):
        ans += 1
print(ans)
