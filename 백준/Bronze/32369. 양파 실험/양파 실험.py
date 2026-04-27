import sys
a = b = 1
t, p, n = map(int, sys.stdin.readline().split())

for _ in range(t):
    a += p
    b += n
    if a < b:
        a, b = b, a
    elif a == b:
        b -= 1
print(a, b)