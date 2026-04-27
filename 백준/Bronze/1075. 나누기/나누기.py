import sys
input = sys.stdin.readline

n = (int(input()) // 100) * 100
f = int(input())
for i in range(100):
    if n % f == 0:
        print(str(n)[-2:])
        break
    n += 1
