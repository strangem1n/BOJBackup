import sys
n = int(sys.stdin.readline())
for _ in range(2):
    for i in range(n):
        print('@'*5*n)
    for i in range(n):
        print('@'*n)
for i in range(n):
    print('@'*n)