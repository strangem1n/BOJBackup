import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = abs((a[-2] + b[-1]) - (b[-2] + a[-1]))
for i in range(n-2):
    result += abs(a[i] - b[i])
print(result)
