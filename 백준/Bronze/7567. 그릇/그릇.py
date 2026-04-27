import sys
n = sys.stdin.readline().rstrip()
ans = 10
for i in range(1, len(n)):
    if n[i] == n[i-1]:
        ans += 5
    else:
        ans += 10
print(ans)