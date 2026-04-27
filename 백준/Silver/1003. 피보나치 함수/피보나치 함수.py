import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        a = 0
        b = 1
        for j in range(n-1):
            a, b = b, b+a
        print(a, b)