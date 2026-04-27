import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = 1
    for _ in range(b):
        ans *= a
        ans %= 10
    if ans == 0:
        ans = 10
    print(ans)