import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = 0
for a in arr:
    res += min(n, a)
print(res)