import sys
input = sys.stdin.readline

def change(x):
    if x == '.':
        return 0
    elif x == 'X':
        return 1
    else:
        return 2

def solve():
    for i in range(10):
        for j in range(10):
            if game[i][j] == 0:
                game[i][j] = 1
                if chk():
                    return 1
                game[i][j] = 0
    return 0

def chk():
    for r in range(10):
        for c in range(10):
            if game[r][c] == 1:
                for k in range(8):
                    for m in range(1, 5):
                        nr, nc = r + (dr[k] * m), c + (dc[k] * m)
                        if 0 <= nr < 10 and 0 <= nc < 10 and game[nr][nc] == 1:
                            continue
                        else:
                            break
                    else:
                        return True
    return False

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]
game = [list(map(change, input().rstrip())) for _ in range(10)]
print(solve())