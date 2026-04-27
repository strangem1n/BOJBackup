import sys
input = sys.stdin.readline

t = int(input())
a = b = 0
for _ in range(t):
    ai, bi = map(int, input().split())
    if ai > bi:
        a += 1
    elif ai < bi:
        b += 1
print(a, b)