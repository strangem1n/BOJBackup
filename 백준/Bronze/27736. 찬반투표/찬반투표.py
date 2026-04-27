import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = e = 0
for a in arr:
    if a == 0:
        e += 1
        continue
    s += a
m = n // 2
if n % 2 == 1:
    m += 1
if e >= m:
    print("INVALID")
elif s <= 0:
    print("REJECTED")
else:
    print("APPROVED")
