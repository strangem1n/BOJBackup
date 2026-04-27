import sys
input = sys.stdin.readline

def solve():
    cnt = 0
    while True:
        temp = cnt
        for i in range(n):
            for j in range(m):
                if i + 2 < n and j + 2 < m and init[i][j] != ans[i][j]:
                    for k in range(3):
                        for l in range(3):
                            init[i + k][j + l] = 1 if init[i + k][j + l] == 0 else 0
                    cnt += 1
        if temp == cnt:
            return chk(cnt)

def chk(c):
    for i in range(n):
        for j in range(m):
            if init[i][j] != ans[i][j]:
                return -1
    return c

n, m = map(int, input().split())
init = [list(map(int, input().rstrip())) for _ in range(n)]
ans = [list(map(int, input().rstrip())) for _ in range(n)]
print(solve())
