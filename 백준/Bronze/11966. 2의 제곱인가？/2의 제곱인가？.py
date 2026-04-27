import sys
input = sys.stdin.readline

def two(n):
    if n == 1:
        return 1
    r = n // 2
    q = n % 2
    if q == 0:
        return two(r)
    else:
        return 0

num = int(input())
print(two(num))