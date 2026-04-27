import sys
input = sys.stdin.readline

result = 0
n = int(input())
for _ in range(n):
    dday = input().rstrip()
    day = int(dday[2:])
    if day <= 90:
        result += 1
print(result)