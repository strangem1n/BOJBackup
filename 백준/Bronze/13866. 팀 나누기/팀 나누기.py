import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
result = abs((a+d)-(b+c))
print(result)