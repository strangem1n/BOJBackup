import sys
n = sys.stdin.readline().rstrip()
num = []
for _ in range(int(n)):
    num.append(int(sys.stdin.readline().rstrip()))
num.sort()
for i in num:
    print(i)