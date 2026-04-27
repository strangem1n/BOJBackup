import sys
input = sys.stdin.readline

def dp(n):
    arr = [0] * n
    arr[0] = arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n-1]

x = int(input())
print(dp(x), x-2)