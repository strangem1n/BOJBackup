import sys
input = sys.stdin.readline

n = int(input())
min_turn = 10001
min_game = 0

for game in range(1, n+1):
    j, m = map(int, input().split())
    turn = (j-1) // (m+1) * 2 + 2
    if min_turn > turn:
        min_turn = turn
        min_game = game
print(min_game, min_turn)
