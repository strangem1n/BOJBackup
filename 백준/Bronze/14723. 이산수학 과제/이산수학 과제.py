import sys
n = int(sys.stdin.readline())
a = 2
b = 0
for _ in range(n):
    if a > 1:
        b += 1
        a -= 1
    else:
        a = b + 1
        b = 1
print(a, b)