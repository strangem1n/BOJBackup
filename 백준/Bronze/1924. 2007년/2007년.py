import sys
x, y = map(int, input().split())
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
while x > 1:
    if x == 3:
        y += 28
    elif x in [2, 4, 6, 8, 9, 11]:
        y += 31
    else:
        y += 30
    x -= 1
print(day[y%7])
