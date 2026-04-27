arr = [sum(map(int, input().split())) for _ in range(5)]
point = 0
winner = 0
for i in range(5):
    if point < arr[i]:
        point = arr[i]
        winner = i+1
print(winner, point)