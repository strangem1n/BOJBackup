import sys
input = sys.stdin.readline

n = int(input())
stack = [int(input()) for _ in range(n)]
prev = ans = 0
while stack:
    r = stack.pop()
    if prev < r:
        prev = r
        ans += 1
print(ans)
