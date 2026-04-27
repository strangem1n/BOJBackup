import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    name = input().rstrip()
    for c in name:
        if c == 'S':
            print(name)
            break