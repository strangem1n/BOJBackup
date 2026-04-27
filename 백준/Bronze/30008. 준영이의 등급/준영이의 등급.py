import sys
input = sys.stdin.readline

def solve(x):
    x = int(x) * 100 // n
    if x <= 4:
        return 1
    elif x <= 11:
        return 2
    elif x <= 23:
        return 3
    elif x <= 40:
        return 4
    elif x <= 60:
        return 5
    elif x <= 77:
        return 6
    elif x <= 89:
        return 7
    elif x <= 96:
        return 8
    else:
        return 9

n, k = map(int, input().split())
score = list(map(solve, input().split()))
print(*score)
