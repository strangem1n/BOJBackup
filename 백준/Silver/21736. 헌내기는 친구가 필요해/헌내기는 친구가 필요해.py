def doyeon(n, m):
    for i in range(n):
        for j in range(m):
            if campus[i][j] == "I":
                return i, j


def move(si, sj, n, m):
    visit = [[0] * m for _ in range(n)]
    queue_i = [0] * (n*m)
    queue_j = [0] * (n*m)
    front = -1
    rear = 0
    queue_i[rear], queue_j[rear] = si, sj
    visit[si][sj] = 1
    meeting = 0
    while front != rear:
        front += 1
        i, j = queue_i[front], queue_j[front]
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and visit[ni][nj] == 0 and campus[ni][nj] != "X":
                rear += 1
                queue_i[rear], queue_j[rear] = ni, nj
                visit[ni][nj] = 1
                if campus[ni][nj] == "P":
                    meeting += 1
    if meeting > 0:
        return meeting
    else:
        return "TT"


n, m = map(int, input().split())
campus = [input() for _ in range(n)]
start_i, start_j = doyeon(n, m)
result = move(start_i, start_j, n, m)
print(result)
