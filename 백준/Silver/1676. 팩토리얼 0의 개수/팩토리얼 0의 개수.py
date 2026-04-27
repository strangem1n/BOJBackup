import math, sys
n = int(sys.stdin.readline())
ans = n // 5 + n // (5**2) + n // (5**3)
print(ans)