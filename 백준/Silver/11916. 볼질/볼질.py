import sys
input = sys.stdin.readline

n = int(input())
arr = map(int, input().split())

score = 0
base = [0, 0, 0]
cnt = 0

for ball in arr:
    if ball == 1:
        cnt += 1
    elif ball == 2:
        cnt = 4
    elif ball == 3:
        cnt += 1
        if base[2] == 1:
            score += 1
            base[2] = 0
        if base[1] == 1:
            base[2] = 1
            base[1] = 0
        if base[0] == 1:
            base[1] = 1
            base[0] = 0

    if cnt == 4:
        cnt = 0
        if base[2] == base[1] == base[0] == 1:
            score += 1
        elif base[1] == base[0] == 1:
            base[2] = 1
        elif base[0] == 1:
            base[1] = 1
        base[0] = 1
print(score)
