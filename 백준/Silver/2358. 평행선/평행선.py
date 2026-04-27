import sys
input = sys.stdin.readline

n = int(input())
x = {}
y = {}
for _ in range(n):
    xi, yi = map(int, input().split())
    if x.get(xi):
        x[xi].append(yi)
    else:
        x[xi] = [yi]
    if y.get(yi):
        y[yi].append(xi)
    else:
        y[yi] = [xi]

result = 0
for xi in x:
    if len(x[xi]) > 1:
        result += 1
for yi in y:
    if len(y[yi]) > 1:
        result += 1
print(result)
