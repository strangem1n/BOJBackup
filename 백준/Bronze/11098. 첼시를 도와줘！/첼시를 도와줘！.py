import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    p = int(input())
    c = 0
    n = None
    for _ in range(p):
        cost, name = input().split()
        if int(cost) > c:
            c = int(cost)
            n = name
    print(n)