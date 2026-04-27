import math
n = int(input())
power = []
a = 0
while a <= 19:
    power.append(2 ** a)
    a += 1

if n in power:
    print(n)
else:
    print(2 * (n - 2 ** int(math.log2(n))))