import sys
input = sys.stdin.readline

n = int(input())
i = ans = 1
while i != n:
    if '50' in str(i):
        ans += 2
    else:
        ans += 1
    i += 1
print(ans)
