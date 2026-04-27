import sys
input = sys.stdin.readline

n = int(input())
arr = map(int, input().split())

chk = -200000
for a in arr:
    if chk <= a:
        print(a, end=' ')
        chk = a