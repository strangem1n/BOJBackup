n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(1<<n):
    sum_part = 0
    for j in range(n):
        if i & (1<<j):
            sum_part += arr[j]
    if s == sum_part:
        result += 1

result = result-1 if s == 0 else result
print(result)