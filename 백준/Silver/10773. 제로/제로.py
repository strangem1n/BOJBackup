n = int(input())
list = [0]
for _ in range(n):
    money = int(input())
    if money != 0:
        list.append(money)
    else:
        list.pop()

ans = 0
for i in list:
    ans += i
print(ans)