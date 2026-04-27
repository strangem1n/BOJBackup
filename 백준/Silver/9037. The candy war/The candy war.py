import sys
from collections import deque
input = sys.stdin.readline

def chk():
    temp = candy[0]
    for c in candy:
        if c != temp:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    candy = list(map(int, input().split()))
    for i in range(n):
        if candy[i] % 2 == 1:
            candy[i] += 1

    cycle = 0
    while not chk():
        cycle += 1
        next_candy = deque(map(lambda x: x // 2, candy))
        next_candy.rotate()
        for i in range(n):
            candy[i] = candy[i] // 2 + next_candy[i]
            if candy[i] % 2 == 1:
                candy[i] += 1
    print(cycle)