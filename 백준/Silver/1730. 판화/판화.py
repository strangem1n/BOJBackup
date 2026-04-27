import sys
input = sys.stdin.readline

n = int(input())
command = input().rstrip()

arr = [["."] * n for _ in range(n)]
i = j = 0
for c in command:
    di = dj = 0
    if c == "U":
        di = -1
    elif c == "D":
        di += 1
    elif c == "L":
        dj -= 1
    else:
        dj += 1
    ni = i + di
    nj = j + dj
    if 0 <= ni < n and 0 <= nj < n:
        if dj == 0:
            arr[i][j] = "+" if arr[i][j] == "-" or arr[i][j] == "+" else "|"
            arr[ni][nj] = "+" if arr[ni][nj] == "-" or arr[ni][nj] == "+" else "|"
        else:
            arr[i][j] = "+" if arr[i][j] == "|" or arr[i][j] == "+" else "-"
            arr[ni][nj] = "+" if arr[ni][nj] == "|" or arr[ni][nj] == "+" else "-"
        i, j = ni, nj

for a in arr:
    print("".join(a))
