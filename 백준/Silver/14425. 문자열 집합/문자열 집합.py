import sys

n, m = map(int, sys.stdin.readline().split())
correct = []
check = []
result = 0

for _ in range(n):
    correct.append(sys.stdin.readline().strip())
for _ in range(m):
    check.append(sys.stdin.readline().strip())

for i in check:
    if i in correct:
        result += 1

print(result)