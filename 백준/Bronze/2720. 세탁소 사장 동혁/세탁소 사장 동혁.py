n = int(input())
items = [25, 10, 5, 1]
for _ in range(n):
    charge = int(input())
    coin = []
    for i in items:
        coins = charge // i
        coin.append(coins)
        charge = charge % i
    print(*coin)