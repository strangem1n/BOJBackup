import sys
input = sys.stdin.readline

n = int(input())
if n < 4:
    print(4)
else:
    if n % 2 == 0:
        print(n)
    else:
        print(n+1)