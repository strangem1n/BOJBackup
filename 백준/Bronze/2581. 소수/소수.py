m = int(input())
n = int(input())
a = []
sum = 0

for i in range(m, n+1):
    a.append(i)
    for j in range(2, i):
        if i % j == 0:
            a.pop()
            break

if 1 in a:
    a.pop(0)

if len(a) >= 1:
    for i in a:
        sum += i
    print(sum)
    print(a[0])
else:
    print(-1)
