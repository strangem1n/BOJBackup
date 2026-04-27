import sys
input = sys.stdin.readline

n = int(input())
result = 6
for i in range(11, n+1):
    result *= i
print(result)