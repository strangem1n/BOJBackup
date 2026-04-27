import sys, math
input = sys.stdin.readline

n = int(input())
m = int(input())
min_power = sum_power = 0
for i in range(int(math.sqrt(n)), int(math.sqrt(m))+1):
    if n <= i**2 <= m:
        if min_power == 0:
            min_power = i**2
        sum_power += i**2
if min_power == 0:
    print(-1)
else:
    print(sum_power)
    print(min_power)
