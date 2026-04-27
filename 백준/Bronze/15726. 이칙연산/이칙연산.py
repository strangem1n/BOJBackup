import sys
a, b, c = map(int, sys.stdin.readline().split())
d = (a*b)//c
e = int((a/b)*c)
print(max(d, e))