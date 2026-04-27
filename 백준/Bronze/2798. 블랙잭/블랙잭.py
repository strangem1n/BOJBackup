n, m = map(int, input().split())
stack = list(map(int, input().split()))
result = []
breaker = False

while True:
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                sum = stack[i]+stack[j]+stack[k]
                if sum <= m:
                    result.append(sum)
                if sum == m:
                    breaker = True
                    break
        if breaker == True:
            break
    if breaker == True:
        break
    break

print(max(result))

