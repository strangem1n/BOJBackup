import sys
input = sys.stdin.readline
a, b = map(int, input().split())
x = (a + b) // 2
if (a + b) % 2 > 0:
    print(-1)
else:
    y = a - x
    if y < 0:
        print(-1)
    else:
        print(x, y)