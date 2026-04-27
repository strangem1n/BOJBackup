import sys
input = sys.stdin.readline

name = map(lambda x: x[0], input().split("-"))
for n in name:
    print(n, end="")