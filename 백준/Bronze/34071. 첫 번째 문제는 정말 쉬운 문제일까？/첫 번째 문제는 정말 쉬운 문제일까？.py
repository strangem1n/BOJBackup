import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))
if arr[0] == min(arr):
    print('ez')
elif arr[0] == max(arr):
    print('hard')
else:
    print('?')
