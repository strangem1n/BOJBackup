import sys
input = sys.stdin.readline

n = int(input())
arr = [[int(input()), i] for i in range(n)]
s = sorted(arr)

max_dis = 0
for i in range(n):
    dis = s[i][1] - i
    if max_dis < dis:
        max_dis = dis
print(max_dis+1)
