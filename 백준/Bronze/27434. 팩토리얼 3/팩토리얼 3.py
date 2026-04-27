import sys
n = int(sys.stdin.readline())
ans = 1
for i in range(1, 1+n):
    ans *= i
print(ans)