n, k = map(int, input().split())
coin = []
for _ in range(n):
    money = int(input())
    coin.append(money)

coin.sort()

ans = 0

while True:
    while True:
        if coin[-1] > k:
            coin.pop()
        else:
            break
    ans += k // coin[-1]
    k = k % coin[-1]
    if k == 0:
        break

print(ans)