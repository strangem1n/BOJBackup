import sys
input = sys.stdin.readline

n = int(input())
cake = 10000
for _ in range(n):
    a, b = map(int, input().split())
    q = b // a
    if cake > q:
        cake = q
print(cake)