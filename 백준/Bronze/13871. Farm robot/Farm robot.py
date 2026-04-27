import sys
input = sys.stdin.readline

n, c, s = map(int, input().split())
arr = list(map(int, input().split()))
start = 1
cnt = 0
for a in arr:
    if start == s:
        cnt += 1
    start += a
    if start < 1:
        start = n
    if start > n:
        start = 1
if start == s:
    cnt += 1
print(cnt)