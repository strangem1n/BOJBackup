a, b, c, d, e, f = map(int, input().split())
breaker = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            breaker = True
            break
    if breaker == True:
        break
print(x, y)