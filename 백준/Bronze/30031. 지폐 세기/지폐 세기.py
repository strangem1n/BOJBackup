import sys
input = sys.stdin.readline

n = int(input())
b = 0
for _ in range(n):
    w, h = map(int, input().split())
    if w == 136:
        b += 1000
    elif w == 142:
        b += 5000
    elif w == 148:
        b += 10000
    elif w == 154:
        b += 50000
print(b)
