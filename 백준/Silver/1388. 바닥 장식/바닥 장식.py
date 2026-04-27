import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            ans += 1
            visited[i][j] = 1
            if arr[i][j] == "-":
                nj = j + 1
                while nj < m:
                    if arr[i][nj] == "-":
                        visited[i][nj] = 1
                        nj += 1
                    else:
                        break
            else:
                ni = i + 1
                while ni < n:
                    if arr[ni][j] == "|":
                        visited[ni][j] = 1
                        ni += 1
                    else:
                        break
print(ans)
