def find_shark(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                return i, j


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
start_i, start_j = find_shark(arr)
arr[start_i][start_j] = 0

shark_size = 2
shark_hungry = 0
move = 0

small_fish_i = [0] * (n ** 2)
small_fish_j = [0] * (n ** 2)
idx = 0

visited = [[0] * n for _ in range(n)]
q = [0] * (n ** 2 + 1)
front = rear = -1
rear += 1
q[rear] = [start_i, start_j]
visited[start_i][start_j] = 1

while True:
    while front != rear:
        front += 1
        go_i, go_j = q[front]
        for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            ni = go_i + di
            nj = go_j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] <= shark_size:
                rear += 1
                q[rear] = [ni, nj]
                visited[ni][nj] = visited[go_i][go_j] + 1
                if 0 < arr[ni][nj] < shark_size:
                    small_fish_i[idx] = ni
                    small_fish_j[idx] = nj
                    idx += 1

    if idx > 0:
        close_fish = n*2 + 1
        close_idx = 0
        for k in range(idx):
            if close_fish > visited[small_fish_i[k]][small_fish_j[k]]:
                close_fish = visited[small_fish_i[k]][small_fish_j[k]]
                close_idx = k
            elif close_fish == visited[small_fish_i[k]][small_fish_j[k]]:
                if small_fish_i[close_idx] > small_fish_i[k]:
                    close_idx = k
                elif small_fish_i[close_idx] == small_fish_i[k]:
                    if small_fish_j[close_idx] > small_fish_j[k]:
                        close_idx = k
        next_i, next_j = small_fish_i[close_idx], small_fish_j[close_idx]
        shark_hungry += 1
        if shark_hungry == shark_size:
            shark_size += 1
            shark_hungry = 0
        move += visited[next_i][next_j] - 1
        front = -1
        rear = 0
        q[rear] = [next_i, next_j]
        visited = [[0] * n for _ in range(n)]
        arr[next_i][next_j] = 0
        visited[next_i][next_j] = 1
        for k in range(idx):
            small_fish_i[k] = 0
            small_fish_j[k] = 0
        idx = 0
    else:
        break

print(move)
