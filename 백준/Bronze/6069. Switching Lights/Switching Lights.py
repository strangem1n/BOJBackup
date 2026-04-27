import sys
input = sys.stdin.readline

n, m = map(int, input().split())
light = [0] * n
for _ in range(m):
    order, start, end = map(int, input().split())
    if order == 0:
        for i in range(start-1, end):
            light[i] = abs(light[i] - 1)
    else:
        print(sum(light[start-1:end]))
        