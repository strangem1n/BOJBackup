import sys
input = sys.stdin.readline

def find_left_up():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                return i, j

def find_length(r, c):
    length = 1
    nr, nc = r, c
    while nr < n-1 and nc < m-1:
        nr += 1
        nc += 1
        if arr[nr][c] == arr[r][nc] == '.':
            return length
        length += 1
    return length

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
si, sj = find_left_up()
k = find_length(si, sj) // 2

if arr[si][sj+k] == '.':
    print('UP')
elif arr[si+k][sj] == '.':
    print('LEFT')
elif arr[si+(k*2)][sj+k] == '.':
    print('DOWN')
elif arr[si+k][sj+(k*2)] == '.':
    print('RIGHT')