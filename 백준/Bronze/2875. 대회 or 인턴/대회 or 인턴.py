import sys

f, m, i = map(int, sys.stdin.readline().split())
team = min(f//2, m)
left = m+f-team*3
if i > left:
    team -= (i-left) // 3
    if (i-left) % 3 > 0:
        team -= 1 
print(team)