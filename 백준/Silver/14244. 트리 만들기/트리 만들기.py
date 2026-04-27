n, m = map(int, input().split())
i = 0
j = 1

for _ in range(n-m):
    print(i, j)
    i += 1
    j += 1

for _ in range(m-1):
    print(i, j)
    j += 1