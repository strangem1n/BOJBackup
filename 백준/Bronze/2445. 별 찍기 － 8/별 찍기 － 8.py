import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    s = "*"*i + " "*(n-i)
    s += s[::-1]
    print(s)
for i in range(n-1, 0, -1):
    s = "*"*i + " "*(n-i)
    s += s[::-1]
    print(s)