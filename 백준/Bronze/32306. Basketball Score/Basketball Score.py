import sys
input = sys.stdin.readline

a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
ta = a1 + a2*2 + a3*3
tb = b1 + b2*2 + b3*3

if ta > tb:
    print(1)
elif ta == tb:
    print(0)
else:
    print(2)