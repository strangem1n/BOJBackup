import sys
input = sys.stdin.readline


def solve(m, n, arr):
    qi = [0] * (m*n)
    qj = [0] * (m*n)
    front = rear = -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                rear += 1
                qi[rear] = i
                qj[rear] = j

    max_day = 1
    while front != rear:
        front += 1
        start_i = qi[front]
        start_j = qj[front]
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
            ni = start_i + di
            nj = start_j + dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0:
                rear += 1
                qi[rear] = ni
                qj[rear] = nj
                arr[ni][nj] = arr[start_i][start_j] + 1
                if max_day < arr[ni][nj]:
                    max_day = arr[ni][nj]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1
    else:
        return max_day-1


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
print(solve(M, N, tomato))
