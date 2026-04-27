import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    n = min(r, c)
    print((n-1)*2)