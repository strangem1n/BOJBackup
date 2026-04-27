x = int(input())
x_ = x
count = 0
while x_ > 0:
    count += 1
    x_ -= count

r = 1 - x_
sum = count + 1

a = str(sum-r)
b = str(r)

if count % 2 == 0:
    print(a+"/"+b)
else:
    print(b+"/"+a)