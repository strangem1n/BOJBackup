import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

max_cost = 0
max_result = 0
for i in range(n):
    cost = (n - i) * arr[i]
    if max_cost < cost:
        max_cost = cost
        max_result = arr[i]
print(max_cost, max_result)
