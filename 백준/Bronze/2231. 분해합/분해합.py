n = int(input())
answer = 0

for i in range(1, n):
    sum = 0
    N = list(str(i))
    for j in N:
        sum += int(j)
    result = i + sum
    if result == n:
        answer = i
        break
    
print(answer)