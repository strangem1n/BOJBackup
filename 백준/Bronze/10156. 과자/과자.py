import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())
require = k * n
print(max(0, require - m))