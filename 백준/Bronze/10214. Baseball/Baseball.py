import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    y = k = 0
    for _ in range(9):
        yi, ki = map(int, input().split())
        y += yi
        k += ki
    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    else:
        print("Draw")