import sys
input = sys.stdin.readline

n = int(input())
board = {}
tiles = list(input().split())
for i in range(n):
    tile = tiles[i]
    if board.get(tile):
        board[tile] += 1
        if board[tile] == 5:
            print(i+1)
            break
    else:
        board[tile] = 1
else:
    print(0)
