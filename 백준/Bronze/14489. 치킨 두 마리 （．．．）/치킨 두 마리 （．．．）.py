import sys
input = sys.stdin.readline

a = sum(map(int, input().split()))
c = int(input())
if a >= c*2:
    print(a-c*2)
else:
    print(a)