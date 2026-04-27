import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    if 6 <= len(p) <= 9:
        print('yes')
    else:
        print('no')
