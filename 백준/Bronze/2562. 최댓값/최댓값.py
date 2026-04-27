import sys
n = list(map(int, sys.stdin.readlines()))
max = max(n)
print(max)
print(n.index(max)+1)