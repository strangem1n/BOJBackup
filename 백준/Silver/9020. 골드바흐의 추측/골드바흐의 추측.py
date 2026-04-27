import sys, math
input = sys.stdin.readline

prime = set()
for i in range(2, 10000):
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        prime.add(i)

t = int(input())
for _ in range(t):
    n = int(input())
    a = b = 0
    for i in range(n//2, 1, -1):
        if i in prime and n-i in prime:
            print(i, n-i)
            break
