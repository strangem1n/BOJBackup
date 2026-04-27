import sys
input = sys.stdin.readline

n, x = map(int, input().split())
latest = -1
for _ in range(n):
    s, t = map(int, input().split())
    if x >= s + t and latest < s:
        latest = s
print(latest)