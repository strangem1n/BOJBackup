import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, *p = input().split()
    n = float(n)
    for i in p:
        if i == "@":
            n *= 3
        elif i == "%":
            n += 5
        else:
            n -= 7
    print(f"{n:.2f}")