import sys
from collections import deque
input = sys.stdin.readline

def solve(n1, n2, n3, n4, m1, m2, m3, m4):
    n = deque([n2, n3, n4])
    if n1 == m1:
        m = deque([m2, m3, m4])
        if chk(n, m):
            return True
    if n1 == m2:
        m = deque([m3, m1, m4])
        if chk(n, m):
            return True
    if n1 == m3:
        m = deque([m4, m1, m2])
        if chk(n, m):
            return True
    if n1 == m4:
        m = deque([m2, m1, m3])
        if chk(n, m):
            return True
    return False

def chk(a, b):
    for _ in range(3):
        if a == b:
            return True
        b.rotate()
    return False

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    if solve(*arr):
        print(1)
    else:
        print(0)
