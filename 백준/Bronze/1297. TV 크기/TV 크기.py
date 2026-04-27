import sys, math
d, h, w = map(int, sys.stdin.readline().split())
print(int(math.sqrt(d**2*(h**2/(h**2+w**2)))), int(math.sqrt(d**2*(w**2/(h**2+w**2)))))