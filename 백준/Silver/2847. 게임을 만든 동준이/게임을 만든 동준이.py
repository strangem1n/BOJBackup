import sys
input = sys.stdin.readline

N = int(input())
level = [int(input()) for _ in range(N)]
result = 0
for i in range(N-1, 0, -1):
    if level[i] > level[i-1]:
        continue
    else:
        diff = level[i-1] - level[i] + 1
        result += diff
        level[i-1] = level[i] - 1
print(result)
