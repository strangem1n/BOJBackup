import sys
input = sys.stdin.readline

min_time = 10000

n = int(input())
for _ in range(n):
    cost, time = map(int, input().split())
    if cost <= time:
        if min_time > time:
            min_time = time

if min_time == 10000:
    print(-1)
else:
    print(min_time)