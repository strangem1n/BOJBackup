import sys
input = sys.stdin.readline

start, end = input().split()
sh, sm = map(int, start.split(':'))
eh, em = map(int, end.split(':'))

limit_h = eh - sh
limit_m = limit_h * 60 + em - sm

n, t = map(int, input().split())

day = time = 0
for _ in range(n+1):
    time += t
    if time >= limit_m:
        day += 1
        time = t

sm += time
sh += sm // 60
sm %= 60
if len(str(sh)) == 1:
    sh = '0' + str(sh)
else:
    sh = str(sh)
if len(str(sm)) == 1:
    sm = '0' + str(sm)
else:
    sm = str(sm)
print(day)
print(f"{sh}:{sm}")