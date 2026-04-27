board = []
newwrite = ""

for _ in range(5):
    write = list(input())
    board.append(write)

for j in range(15):
    for i in range(5):
        try:
            newwrite += board[i][j]
        except IndexError:
            pass

print(newwrite)