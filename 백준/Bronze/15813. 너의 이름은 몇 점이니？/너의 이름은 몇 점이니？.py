import sys
input = sys.stdin.readline
n = int(input())
name = input().rstrip()
ans = 0
for i in range(n):
    ans += ord(name[i]) - 64
print(ans)
