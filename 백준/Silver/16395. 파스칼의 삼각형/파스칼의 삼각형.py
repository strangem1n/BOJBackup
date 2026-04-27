import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0] * 30 for _ in range(30)]
for i in range(30):
    arr[i][0] = 1
    arr[i][i] = 1
for i in range(2, 30):
    for j in range(1, i):
        arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
print(arr[n-1][k-1])
