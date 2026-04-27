n, m, a, b = map(int, input().split())
if n*3 <= m:
    print(0)
else:
    print((n*3-m)*a+b)