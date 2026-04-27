import sys
input = sys.stdin.readline
a, n = "", 0
for _ in range(7):
    b, m = input().split()
    m = int(m)
    if m > n:
        a, n = b, m
print(a)