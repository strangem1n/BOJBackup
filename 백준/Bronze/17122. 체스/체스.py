import sys
input = sys.stdin.readline
chess = {}
for i in range(8):
    for j in range(1, 9):
        if i % 2 == 1:
            if j % 2 == 1:
                chess[i*8+j] = 0
            else:
                chess[i*8+j] = 1
        else:
            if j % 2 == 1:
                chess[i*8+j] = 1
            else:
                chess[i*8+j] = 0

n = int(input())
for _ in range(n):
    a, b = input().split()
    d = int(b)
    c = (int(a[1]) - 1) * 8 + ord(a[0]) - 64
    if chess[c] == chess[d]:
        print('YES')
    else:
        print('NO')
