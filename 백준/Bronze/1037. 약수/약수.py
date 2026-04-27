import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if n % 2 == 1:
    print(arr[n//2]**2)
else:
    print(arr[0]*arr[-1])