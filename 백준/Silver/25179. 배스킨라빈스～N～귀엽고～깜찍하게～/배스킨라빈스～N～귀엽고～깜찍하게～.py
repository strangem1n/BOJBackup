import sys
a, b = map(int, sys.stdin.readline().split())
if (a-1) % (b+1) > 0:
    print("Can win")
else:
    print("Can't win")