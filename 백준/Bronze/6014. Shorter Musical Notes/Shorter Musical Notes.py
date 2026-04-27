import sys
input = sys.stdin.readline

n, m = map(int, input().split())
song = [0] * 1200001
idx = 0
for i in range(1, n+1):
    b = int(input())
    for _ in range(b):
        song[idx] = i
        idx += 1
for _ in range(m):
    q = int(input())
    print(song[q])
