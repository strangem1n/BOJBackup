import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visit = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]
    q = deque([(0, 0, k)])
    visit[0][0][0] = 1
    while q:
        i, j, horse = q.popleft()
        if i == h-1 and j == w-1:
            return visit[i][j][k-horse]-1
        if horse > 0:
            for di, dj in jump:
                ni, nj = i+di, j+dj
                if 0 <= ni < h and 0 <= nj < w and visit[ni][nj][k-horse+1] == 0 and arr[ni][nj] == 0:
                    q.append((ni, nj, horse-1))
                    visit[ni][nj][k-horse+1] = visit[i][j][k-horse] + 1
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w and visit[ni][nj][k-horse] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj, horse))
                visit[ni][nj][k-horse] = visit[i][j][k-horse]+1
    return -1


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
jump = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
print(bfs())
