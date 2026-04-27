import sys
input = sys.stdin.readline
board = [input().rstrip() for _ in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and board[i][j] == "F":
            ans += 1
print(ans)
