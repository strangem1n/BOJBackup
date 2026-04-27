import sys
input = sys.stdin.readline
n = 1
for _ in range(3):
    n *= int(input())
arr = [0] * 10
for i in str(n):
    arr[int(i)] += 1
for a in arr:
    print(a)
