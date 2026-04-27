import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(7)]
odd = []

for a in arr:
    if a % 2 == 1:
        odd.append(a)

if len(odd) > 0:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)