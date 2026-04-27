import sys
n, m = sys.stdin.read().split()
n = n[2] + n[1] + n[0]
m = m[2] + m[1] + m[0]
if int(n) > int(m):
    print(int(n))
else:
    print(int(m))