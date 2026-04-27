import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        r, c = q.popleft()
        for z in range(4):
            nr, nc = r + dr[z], c + dc[z]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and abs(arr[r][c] - arr[nr][nc]) <= k:
                visited[nr][nc] = 1
                q.append((nr, nc))

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
