import sys
input = sys.stdin.readline

ans = 0
for _ in range(10):
    n = int(input())
    if abs(100-ans) >= abs(100-(ans+n)):
        ans += n
    else:
        break
print(ans)
