import sys
inp = lambda: sys.stdin.readline().rstrip()
n = int(inp())
for _ in range(n):
    a, b = map(int, inp().split())
    print(a+b)