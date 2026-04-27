import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
longest = days = 0
forget = -1
item = True
for i in range(n):
    if forget == i:
        item = True
    if arr[i] > 0:
        days += 1
    else:
        if item:
            item = False
            forget = i + 2
        else:
            if longest < days:
                longest = days
            days = 0
if longest < days:
    longest = days
print(longest)
