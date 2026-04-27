import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = max(a, b, c)
print(3*d-(a+b+c))