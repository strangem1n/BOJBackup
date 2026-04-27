import sys, math

a, b, v = map(int, sys.stdin.readline().split())

day = (v - a) / (a - b) + 1
day = math.ceil(day)

print(day)