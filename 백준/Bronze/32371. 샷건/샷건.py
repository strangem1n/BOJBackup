import sys
input = sys.stdin.readline

def fill(ch):
    for i in range(4):
        for j in range(10):
            if keyboard[i][j] == ch:
                arr[i][j] = True
                return

def solve():
    for i in range(4):
        for j in range(10):
            if arr[i][j]:
                return keyboard[i+1][j+1]

keyboard = [list(input().rstrip()) for _ in range(4)]
arr = [[False] * 10 for _ in range(4)]
crash = input().rstrip()
for c in crash:
    fill(c)
print(solve())
