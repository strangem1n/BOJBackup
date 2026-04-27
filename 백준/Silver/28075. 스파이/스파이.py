import sys
input = sys.stdin.readline

def solve(day, total, prev):
    global result
    if day == n:
        if total >= m:
            result += 1
    else:
        for i in range(2):
            for j in range(3):
                if j == prev:
                    solve(day+1, total+(score[i][j]//2), j)
                else:
                    solve(day+1, total+(score[i][j]), j)

n, m = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(2)]
result = 0
solve(0, 0, -1)
print(result)