import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q, *queen = map(int, input().split())
k, *knight = map(int, input().split())
p, *pawn = map(int, input().split())

board = [[0] * m for _ in range(n)]
for i in range(q):
    board[queen[i*2]-1][queen[i*2+1]-1] = 2
for i in range(k):
    board[knight[i*2]-1][knight[i*2+1]-1] = 3
for i in range(p):
    board[pawn[i*2]-1][pawn[i*2+1]-1] = 4

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
for i in range(q):
    qi, qj = queen[i*2]-1, queen[i*2+1]-1
    for r in range(8):
        ni, nj = qi + di[r], qj + dj[r]
        while 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj] < 2:
                board[ni][nj] = 1
                ni += di[r]
                nj += dj[r]
            else:
                break

ji = [1, 2, 2, 1, -1, -2, -2, -1]
jj = [2, 1, -1, -2, -2, -1, 1, 2]
for i in range(k):
    ki, kj = knight[i*2]-1, knight[i*2+1]-1
    for r in range(8):
        ni, nj = ki + ji[r], kj + jj[r]
        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] < 2:
            board[ni][nj] = 1

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            result += 1
print(result)
