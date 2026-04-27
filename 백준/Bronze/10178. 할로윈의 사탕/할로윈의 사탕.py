import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(f"You get {n//m} piece(s) and your dad gets {n%m} piece(s).")