n = int(input())
trophy = [int(input()) for _ in range(n)]
left_max, right_max, left_view, right_view = 0, 0, 0, 0
for i in range(n):
    if left_max < trophy[i]:
        left_max = trophy[i]
        left_view += 1
    if right_max < trophy[-(i+1)]:
        right_max = trophy[-(i+1)]
        right_view += 1
print(left_view)
print(right_view)
