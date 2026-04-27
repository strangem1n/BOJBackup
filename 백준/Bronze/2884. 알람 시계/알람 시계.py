a, b = input().split()
hour = int(a)
min = int(b) - 45
if min < 0:
    hour -= 1
    min += 60
    if hour < 0:
        hour += 24
print (hour, min)