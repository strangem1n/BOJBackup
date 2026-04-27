import sys
from collections import deque
input = sys.stdin.readline

def down_dimension(x, y):
    return x * c + y

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        x, y = y, x
    parent[x] = y

def change(x):
    if x == '.':
        return 0
    elif x == 'X':
        return 1
    else:
        return 2

def chk():
    x_duck = down_dimension(*duck[0])
    y_duck = down_dimension(*duck[1])
    if find(x_duck) == find(y_duck):
        return True
    else:
        return False

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
r, c = map(int, input().split())
arr = [list(map(change, input().rstrip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
parent = list(range(r*c))
q = deque([])
duck = []

temp_q = deque([])
for i in range(r):
    for j in range(c):
        if arr[i][j] != 1:
            if arr[i][j] == 2:
                duck.append((i, j))
            visited[i][j] = 1
            temp_q.append([i, j])
            while temp_q:
                qi, qj = temp_q.popleft()
                qij = down_dimension(qi, qj)
                for k in range(4):
                    ni, nj = qi + di[k], qj + dj[k]
                    if 0 <= ni < r and 0 <= nj < c and visited[ni][nj] == 0:
                        if arr[ni][nj] != 1:
                            visited[ni][nj] = 1
                            nij = down_dimension(ni, nj)
                            union(qij, nij)
                            temp_q.append([ni, nj])
                        else:
                            q.append([qi, qj])
                            break

day = 0
while True:
    for i, j in q:
        ij = down_dimension(i, j)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < r and 0 <= nj < c and visited[ni][nj] == 1:
                nij = down_dimension(ni, nj)
                union(ij, nij)
    if chk():
        print(day)
        break
    for _ in range(len(q)):
        qi, qj = q.popleft()
        qij = down_dimension(qi, qj)
        for k in range(4):
            ni, nj = qi + di[k], qj + dj[k]
            if 0 <= ni < r and 0 <= nj < c:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append([ni, nj])
                nij = down_dimension(ni, nj)
                union(qij, nij)
    day += 1
