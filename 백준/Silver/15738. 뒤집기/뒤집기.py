import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
__ = input()
for _ in range(m):
    i = int(input())
    if i > 0:
        for idx in range(i//2):
            arr[idx], arr[i-(1+idx)] = arr[i-(1+idx)], arr[idx]
    else:
        for idx in range(1, (-i//2)+1):
            arr[-idx], arr[n+i+(idx-1)] = arr[n+i+(idx-1)], arr[-idx]
for i in range(n):
    if arr[i] == k:
        print(i+1)
        break
