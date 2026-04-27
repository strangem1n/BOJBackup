import sys
a = sys.stdin.readline().rstrip()
ans = 0
for i in a:
    if i in ['a', 'e', 'i', 'o', 'u']:
        ans += 1
print(ans)
