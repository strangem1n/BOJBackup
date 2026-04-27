import sys
input = sys.stdin.readline

def solve():
    global ari
    for m in move:
        ari_i, ari_j, ari_di, ari_dj = ari
        lighten()

        if m == "F":
            ari_ni, ari_nj = ari_i + ari_di, ari_j + ari_dj
            if 0 <= ari_ni < n and 0 <= ari_nj < n:
                ari = [ari_ni, ari_nj, ari_di, ari_dj]
                lighten()
            else:
                ari = [ari_i, ari_j, ari_di, ari_dj]
        else:
            c = 0
            for k in range(4):
                if d[k][0] == ari_di and d[k][1] == ari_dj:
                    c = k
            if m == "L":
                ari = [ari_i, ari_j, d[(c+1)%4][0], d[(c+1)%4][1]]
            else:
                ari = [ari_i, ari_j, d[(c+3)%4][0], d[(c+3)%4][1]]

        if meet():
            return "Aaaaaah!"
        for zn in range(len(zombie)):
            zi, zj, zd = zombie[zn]
            if 0 <= zi + zd < n:
                zombie[zn][0] = zi + zd
            else:
                zombie[zn][2] *= -1
        if meet():
            return "Aaaaaah!"
    return "Phew..."

def lighten():
    if arr[ari[0]][ari[1]] == "S":
        light[ari[0]][ari[1]] = True
        for di, dj in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
            ni, nj = ari[0] + di, ari[1] + dj
            if 0 <= ni < n and 0 <= nj < n:
                light[ni][nj] = True

def meet():
    for zi, zj, zd in zombie:
        if not light[ari[0]][ari[1]] and ari[0] == zi and ari[1] == zj:
            return True
    return False

n = int(input())
move = input().rstrip()
arr = [list(input().rstrip()) for _ in range(n)]
zombie = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "Z":
            zombie.append([i, j, 1])

ari = [0, 0, 1, 0]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
light = [[False] * n for _ in range(n)]
print(solve())