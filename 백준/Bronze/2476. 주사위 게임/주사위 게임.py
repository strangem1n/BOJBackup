import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        money = a * 1000 + 10000
    elif a != b and b != c and c != a:
        money = max(a, b, c) * 100
    else:
        if a == b or a == c:
            money = a * 100 + 1000
        else:
            money = b * 100 + 1000
    ans = max(ans, money)
print(ans)