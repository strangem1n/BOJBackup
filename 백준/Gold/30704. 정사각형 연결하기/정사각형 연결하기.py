import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    base = int(math.sqrt(n))
    add = n - (base ** 2)
    if add == 0:
        print(4*base)
    elif add <= base:
        print(4*base+2)
    else:
        print(4*base+4)
