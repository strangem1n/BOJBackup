import sys
input = sys.stdin.readline

s = list(map(int, input().split()))
e = list(map(int, input().split()))

y = e[0] - s[0]
m = e[1] - s[1]
d = e[2] - s[2]

if d < 0:
    m -= 1
    d += 30
if m < 0:
    y -= 1
    m += 12

yearly = cnt = bonus = 0
for i in range(y):
    yearly += 15 + bonus
    cnt += 1
    if cnt == 2:
        cnt = 0
        bonus += 1

monthly = min(y*12+m, 36)

print(yearly, monthly)
print(f"{y*360+m*30+d}days")
