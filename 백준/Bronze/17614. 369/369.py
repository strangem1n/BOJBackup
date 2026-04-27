import sys
n = int(sys.stdin.readline())

cnt = 0
for i in range(1, n+1):
    while i > 0:
        j = i % 10
        if j == 3 or j == 6 or j == 9:
            cnt += 1
        i //= 10
print(cnt)
