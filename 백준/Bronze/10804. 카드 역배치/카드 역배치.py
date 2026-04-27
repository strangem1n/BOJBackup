import sys
n = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())
    n = n[:a] + n[a:b+1][::-1] + n[b+1:]
print(*n[1:])
