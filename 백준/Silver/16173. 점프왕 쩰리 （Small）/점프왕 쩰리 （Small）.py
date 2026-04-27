import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
q = deque([(0, 0)])
visited[0][0] = 1
while q:
    i, j = q.popleft()
    ni, nj = i + arr[i][j], j + arr[i][j]
    if ni < n and visited[ni][j] == 0:
        visited[ni][j] = 1
        q.append((ni, j))
    if nj < n and visited[i][nj] == 0:
        visited[i][nj] = 1
        q.append((i, nj))
if visited[n-1][n-1] == 1:
    print("HaruHaru")
else:
    print("Hing")
