import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
line = [None] * n
for i in range(n):
    if not line[arr[i]]:
        line[arr[i]] = i + 1
    else:
        line.pop()
        line = line[:arr[i]] + [i+1] + line[arr[i]:]
print(*line[::-1])
