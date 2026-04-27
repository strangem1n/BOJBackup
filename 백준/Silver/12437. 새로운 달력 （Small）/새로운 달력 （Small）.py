import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    month, day, week = map(int, input().split())
    total = day * month
    result = 0
    q = 0

    for _ in range(month):
        this_month = day
        if q > 0:
            this_month -= q
            result += 1
        result += this_month // week
        q = this_month % week
        if q > 0:
            q = week - q
            result += 1
    print(f"Case #{tc}: {result}")
