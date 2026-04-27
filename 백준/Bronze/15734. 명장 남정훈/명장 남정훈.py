import sys
l, r, a = map(int, sys.stdin.readline().split())

while a > 0:
    if l < r:
        l += 1
        a -= 1
    else:
        r += 1
        a -= 1
print(min(l, r)*2)