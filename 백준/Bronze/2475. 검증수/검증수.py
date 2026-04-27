num = list(map(int, input().split()))
check = 0
for i in num:
    check += i ** 2
print(check % 10)