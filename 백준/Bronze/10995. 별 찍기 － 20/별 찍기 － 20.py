import sys
n = int(sys.stdin.readline())

star = ["* " * n]
star_i = [" *" * n]
for i in range(n):
    if i % 2 == 0:
        print(*star, sep="")
    else:
        print(*star_i, sep="")
