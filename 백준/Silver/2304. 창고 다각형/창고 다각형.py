def solve(N, middle):
    area = 0
    left_start, left_length = arr[0]
    i = 1
    while left_length != middle:
        if left_length < arr[i][1]:
            area += (arr[i][0] - left_start) * left_length
            left_start, left_length = arr[i]
        i += 1

    right_start, right_length = arr[N-1]
    j = N-2
    while right_length != middle:
        if right_length < arr[j][1]:
            area += (right_start - arr[j][0]) * right_length
            right_start, right_length = arr[j]
        j -= 1

    i -= 1
    j += 1
    area += (arr[j][0] + 1 - arr[i][0]) * middle
    return area


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n-1):
    min_num = arr[i][0]
    min_idx = i
    for j in range(i+1, n):
        if min_num > arr[j][0]:
            min_num = arr[j][0]
            min_idx = j
    if i != min_idx:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

max_length = 0
for i in range(n):
    if max_length < arr[i][1]:
        max_length = arr[i][1]
result = solve(n, max_length)
print(result)
