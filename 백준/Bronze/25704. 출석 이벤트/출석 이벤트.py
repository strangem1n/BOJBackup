import sys
input = sys.stdin.readline

n = int(input())
discount = n // 5
price = int(input())
arr = [price]
if discount > 0:
    arr.append(max(price-500, 0))
if discount > 1:
    arr.append(price*9//10)
if discount > 2:
    arr.append(max(price-2000, 0))
if discount > 3:
    arr.append(price*3//4)
print(min(arr))