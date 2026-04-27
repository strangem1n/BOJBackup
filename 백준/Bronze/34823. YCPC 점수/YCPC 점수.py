import sys
y, c, p = map(int, sys.stdin.readline().split())
print(min(y, c//2, p))