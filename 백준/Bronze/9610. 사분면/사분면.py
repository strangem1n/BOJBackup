import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 5
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        arr[4] += 1
    elif x > 0 and y > 0:
        arr[0] += 1
    elif x < 0 and y < 0:
        arr[2] += 1
    elif x < 0 and y > 0:
        arr[1] += 1
    else:
        arr[3] += 1
print(f"Q1: {arr[0]}", f"Q2: {arr[1]}", f"Q3: {arr[2]}", f"Q4: {arr[3]}", f"AXIS: {arr[4]}", sep="\n")
