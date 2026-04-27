import sys
input = sys.stdin.readline
cup = [0, 1, 0, 0]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    cup[a], cup[b] = cup[b], cup[a]
for i in range(1, 4):
    if cup[i] == 1:
        print(i)
