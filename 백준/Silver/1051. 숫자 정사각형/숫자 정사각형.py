n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
max_area = 1
for i in range(n):
    for j in range(m):
        for k in range(1, max(n, m)):
            ni = i + k*1
            nj = j + k*1
            if 0 <= ni < n and 0 <= nj < m:
                if arr[i][j] == arr[ni][j] == arr[i][nj] == arr[ni][nj]:
                    length = k+1
                    if max_area < length ** 2:
                        max_area = length ** 2
print(max_area)

