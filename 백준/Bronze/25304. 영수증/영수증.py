sum = 0
total = int(input())
kind = int(input())
for _ in range(kind):
    item, num = map(int, input().split())
    price = item * num
    sum += price
if sum == total:
    print("Yes")
else:
    print("No")