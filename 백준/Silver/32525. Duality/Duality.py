import sys
input = sys.stdin.readline
C = 10**8

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n+1):
        x, y = map(int, input().split())
        if y >= 0:
            print(i, x+1, y+(C+1))
        else:
            print(i, x+1, y-(C+1))
