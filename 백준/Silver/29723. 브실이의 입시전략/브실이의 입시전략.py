import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
score = {}
for _ in range(n):
    sub, s = input().split()
    score[sub] = int(s)
known = 0
for _ in range(k):
    sub = input().rstrip()
    known += score[sub]
    score[sub] = 101
board = sorted(score.values())
while board and board[-1] == 101:
    board.pop()
r = m - k
mn = mx = 0
for i in range(r):
    mn += board[i]
    mx += board[-(i+1)]
print(known+mn, known+mx)
