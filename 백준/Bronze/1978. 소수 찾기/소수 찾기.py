n = int(input())
num = list(map(int, input().split()))
max = max(num)
a = []
result = 0

for i in range(2, max+1):
    a.append(i)
    for j in range(2, i):
        if i % j == 0:
            a.pop()
            break

for i in range(n):
    if a.count(num[i]) == 1:
        result += 1

print(result)