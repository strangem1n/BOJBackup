import sys
n = int(sys.stdin.readline())
if n == 1:
    print("*")
else:
    s = ["*", " "]
    for i in range(n-1):
        s[(0+i)%2] += " "
        s[(1+i)%2] += "*"
    for i in range(n):
        for si in s:
            print(si)
