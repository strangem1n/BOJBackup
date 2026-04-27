import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    q = deque([[i, j]])
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < r and 0 <= nj < c and maze[ni][nj] != 'X':
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])
                if maze[ni][nj] == 'G':
                    return visited[ni][nj] - 1
    return -1

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    r, c = map(int, input().split())
    maze = [input().rstrip() for _ in range(r)]
    visited = [[0] * c for _ in range(r)]
    for m in range(r):
        for n in range(c):
            if maze[m][n] == 'S':
                result = bfs(m, n)
    if result == -1:
        print('No Exit')
    else:
        print(f'Shortest Path: {result}')