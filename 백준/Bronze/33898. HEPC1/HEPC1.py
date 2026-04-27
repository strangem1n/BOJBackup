import sys
input = sys.stdin.readline

def ccw(i, j, word):
    global result
    if len(word) == 4:
        if word == 'HEPC':
            result = True
    else:
        if i == j == 0:
            ccw(i, j+1, word+board[i][j])
            ccw(i+1, j, word + board[i][j])
        elif i == 0 and j == 1:
            ccw(i+1, j, word+board[i][j])
            ccw(i, j-1, word+board[i][j])
        elif i == j == 1:
            ccw(i, j-1, word+board[i][j])
            ccw(i-1, j, word+board[i][j])
        elif i == 1 and j == 0:
            ccw(i-1, j, word+board[i][j])
            ccw(i, j+1, word+board[i][j])

board = [input().rstrip() for _ in range(2)]
result = False
for r in range(2):
    for c in range(2):
        ccw(r, c, '')
        if result:
            print('YES')
            break
    if result:
        break
if not result:
    print('NO')
