import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = map(int, input().split())
    s = 0
    m = float('inf')
    for a in n:
        if a % 2 == 0:
            s += a
            if m > a:
                m = a
    print(s, m)