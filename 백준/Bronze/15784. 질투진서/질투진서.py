import sys
input = sys.stdin.readline

def solve():
    h = arr[r-1][c-1]
    for i in range(n):
        if arr[i][c-1] > h:
            return "ANGRY"
    for j in range(n):
        if arr[r-1][j] > h:
            return "ANGRY"
    return "HAPPY"

n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solve())
