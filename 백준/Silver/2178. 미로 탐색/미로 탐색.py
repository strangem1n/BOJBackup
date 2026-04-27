n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]
q_row = [''] * (n*m+1)
q_column = [''] * (n*m+1)
front = rear = -1
rear += 1
q_row[rear], q_column[rear] = 0, 0
while front != rear:
    front += 1
    r, c = q_row[front], q_column[front]
    for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == 1:
            rear += 1
            q_row[rear], q_column[rear] = nr, nc
            maze[nr][nc] = maze[r][c] + 1
print(maze[n-1][m-1])
