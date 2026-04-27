import sys
input = sys.stdin.readline

n = int(input())
zoo = [input().rstrip() for _ in range(n)]

result = 0
for i in range(n):
    if zoo[-(i+1)] == 'O':
        result += 2 ** i
print(result)