import math, sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
limit = math.sqrt(a ** 2 + b ** 2)
for _ in range(n):
    match = int(input())
    if match > limit:
        print('NE')
    else:
        print('DA')