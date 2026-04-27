n = int(input())
mine = [list(input()) for _ in range(n)]
play = [list(input()) for _ in range(n)]
result = [[0]*n for _ in range(n)]

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if mine[i][j] == '*':
            result[i][j] = '*'
        else:
            danger = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and mine[ni][nj] == '*':
                    danger += 1
            result[i][j] = danger

survive = True
for i in range(n):
    for j in range(n):
        if play[i][j] == '.':
            result[i][j] = '.'
        elif play[i][j] == 'x' and mine[i][j] == '*':
            survive = False

if not survive:
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '*':
                result[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(result[i][j], end='')
    print('')
