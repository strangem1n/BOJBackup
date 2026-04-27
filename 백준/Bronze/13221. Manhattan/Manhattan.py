import sys
input = sys.stdin.readline

x, y = map(int, input().split())
t = int(input())
min_distance = float('inf')
min_x = min_y = 0
for _ in range(t):
    x1, y1 = map(int, input().split())
    distance = abs(x - x1) + abs(y - y1)
    if min_distance > distance:
        min_distance = distance
        min_x = x1
        min_y = y1
print(min_x, min_y)