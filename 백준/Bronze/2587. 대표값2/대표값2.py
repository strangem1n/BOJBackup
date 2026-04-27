num = []
for _ in range(5):
    num.append(int(input()))
num.sort()
sum = 0
for i in num:
    sum += i
avg = int(sum/len(num))
print(avg)
print(num[2])