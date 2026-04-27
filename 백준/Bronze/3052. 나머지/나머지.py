import sys

num = list(map(int, sys.stdin.readlines()))
remainder = set()
R = 0

for i in num:
    R = i % 42
    remainder.add(R)

print(len(remainder))