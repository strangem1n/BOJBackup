import sys
from collections import deque
input = sys.stdin.readline

def down_dimension(x, y):
    return x * n + y

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a

def chk():
    save = -1
    for xy in init:
        if save == -1:
            save = find(xy)
        else:
            if save != find(xy):
                return False
    return True

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

n, k = map(int, input().split())
visited = [[0] * n for _ in range(n)]
q = deque([])
parent = list(range(n**2))
rank = [0] * (n**2)
init = []
for i in range(1, k+1):
    r, c = map(int, input().split())
    q.append([r-1, c-1])
    idx = down_dimension(r-1, c-1)
    init.append(idx)
    rank[idx] = i
    visited[r-1][c-1] = 1

day = 0
while True:
    for r, c in q:
        rc = down_dimension(r, c)
        for d in range(4):
            nr, nc = r + di[d], c + dj[d]
            if 0 <= nr < n and 0 <= nc < n:
                nrc = down_dimension(nr, nc)
                prc = rank[find(rc)]
                pnrc = rank[find(nrc)]
                if prc > 0 and pnrc > 0 and prc != pnrc:
                    union(rc, nrc)
    if chk():
        print(day)
        break
    for i in range(len(q)):
        r, c = q.popleft()
        rc = down_dimension(r, c)
        for d in range(4):
            nr, nc = r + di[d], c + dj[d]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                nrc = down_dimension(nr, nc)
                visited[nr][nc] = 1
                union(nrc, rc)
                q.append([nr, nc])
    day += 1
