import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a + b >= 50:
        print(49)
    else:
        print(a+b+1)