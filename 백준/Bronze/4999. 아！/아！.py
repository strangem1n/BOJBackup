import sys
input = sys.stdin.readline
j = len(input().rstrip())
d = len(input().rstrip())
if j < d:
    print("no")
else:
    print("go")