import sys
input = sys.stdin.readline

n = input().rstrip()
s = list(map(int, n))
if 0 in s and sum(s) % 3 == 0:
    for i in sorted(s, reverse=True):
        print(i, end="")
else:
    print(-1)
