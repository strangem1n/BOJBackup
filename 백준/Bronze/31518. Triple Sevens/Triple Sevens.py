import sys
input = sys.stdin.readline
n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
if 7 in first and 7 in second and 7 in third:
    print(777)
else:
    print(0)
