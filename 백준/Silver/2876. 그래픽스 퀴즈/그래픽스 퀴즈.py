import sys
input = sys.stdin.readline

n = int(input())
desk = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 5 for _ in range(n)]
dp[0][desk[0][0]-1] = 1
dp[0][desk[0][1]-1] = 1
for i in range(1, n):
    for j in range(2):
        dp[i][desk[i][j]-1] = dp[i-1][desk[i][j]-1] + 1

grade = 6
student = 0
for i in range(n):
    for j in range(5):
        if dp[i][j] > student:
            grade = j + 1
            student = dp[i][j]
        elif dp[i][j] == student:
            grade = min(grade, j + 1)
print(student, grade)
