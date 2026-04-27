import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
m = n//2 if n % 2 != 0 else (n//2)-1
print(arr[m])
