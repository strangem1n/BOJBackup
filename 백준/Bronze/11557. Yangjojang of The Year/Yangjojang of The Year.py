import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans = ""
    b = 0
    for _ in range(n):
        name, bottle = input().split()
        bottle = int(bottle)
        if b < bottle:
            ans = name
            b = bottle
    print(ans)
