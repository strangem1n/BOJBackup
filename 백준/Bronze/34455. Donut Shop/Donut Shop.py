import sys
input = sys.stdin.readline
i = int(input())
day = int(input())
for _ in range(day):
    m = input().rstrip()
    n = int(input())
    if m == "+":
        i += n
    else:
        i -= n
print(i)
