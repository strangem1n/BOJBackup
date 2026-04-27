import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    sale = 0
    for i in range(2, n, 3):
        sale += arr[i]
    print(sale)
