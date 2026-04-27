import sys
input = sys.stdin.readline

def solve(idx):
    temp_x, temp_y = x[idx], y[idx]
    x[idx], y[idx] = 0, 0
    max_x, max_y = max(x), max(y)
    x[idx], y[idx] = 40001, 40001
    min_x, min_y = min(x), min(y)
    x[idx], y[idx] = temp_x, temp_y
    return (max_y - min_y) * (max_x - min_x)

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

min_result = float('inf')
for i in range(n):
    result = solve(i)
    if min_result > result:
        min_result = result
print(min_result)