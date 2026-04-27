def minus(a, b):
    if a - b < 0:
        return 0
    else:
        return 1 + minus(b, a-b)


n = int(input())
max_result = 0
n2 = 0
for i in range(1, n+1):
    result = minus(n, i)
    if max_result < result:
        max_result = result
        n2 = i
print(max_result+2)
print(n, end=' ')
print(n2, end=' ')
while n - n2 > -1:
    n -= n2
    print(n, end=' ')
    n, n2 = n2, n
