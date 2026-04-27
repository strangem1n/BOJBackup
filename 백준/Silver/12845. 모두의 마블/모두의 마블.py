import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()), reverse=True)
result = 0
for i in range(1, n):
    result += arr[0] + arr[i]
print(result)
