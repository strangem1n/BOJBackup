import sys
input = sys.stdin.readline

def solve(idx):
    i = idx
    for j in range(1, n):
        i += 1
        if i == n:
            i = 0
        if puzzle[i] != origin[j]:
            break
    else:
        return "good puzzle"

    i = idx
    for j in range(1, n):
        i -= 1
        if i == -1:
            i = n - 1
        if puzzle[i] != origin[j]:
            break
    else:
        return "good puzzle"
    return "bad puzzle"

n = int(input())
origin = list(map(int, input().split()))
puzzle = list(map(int, input().split()))
k = puzzle.index(origin[0])
print(solve(k))
