import sys
gugu = set()
for i in range(1, 10):
    for j in range(1, 10):
        gugu.add(i*j)
n = int(sys.stdin.readline())
if n in gugu:
    print(1)
else:
    print(0)