a, b = input().split()
cook = int(input())
hour = int(a)
min = int(b) + cook
while min >= 60:
    hour += 1
    min -= 60
    if hour >= 24:
        hour = 24 - hour
print(hour, min)
