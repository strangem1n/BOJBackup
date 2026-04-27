import sys
a = map(int, sys.stdin.readline().split())
result = 0
for n in a:
    if n > 0:
        result += 1
print(result)