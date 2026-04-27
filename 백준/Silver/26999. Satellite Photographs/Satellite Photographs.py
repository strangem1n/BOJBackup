import sys
input = sys.stdin.readline

w, h = map(int, input().split())
arr = [input().rstrip() for _ in range(h)]
visited = [[0] * w for _ in range(h)]

def dfs(i, j):
    if visited[i][j] > 0:
        return 0

    stack = [[i, j]]
    cnt = 1
    visited[i][j] = cnt
    while stack:
        i, j = stack[-1]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < h and 0 <= nj < w:
                if arr[ni][nj] == '*' and visited[ni][nj] == 0:
                    cnt += 1
                    visited[ni][nj] = cnt
                    stack.append([ni, nj])
                    break
        else:
            stack.pop()
    return cnt

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

max_field = 0
for r in range(h):
    for c in range(w):
        if arr[r][c] == '*':
            field = dfs(r, c)
            max_field = max(max_field, field)
print(max_field)