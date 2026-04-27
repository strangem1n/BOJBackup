import sys
from collections import deque
input = sys.stdin.readline


d = deque()

N = int(input())
for _ in range(N):
    order = input().rstrip()
    if order[0] == "1":
        a, x = map(int, order.split())
        d.appendleft(x)
    elif order[0] == "2":
        a, x = map(int, order.split())
        d.append(x)
    elif order == "3":
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif order == "4":
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif order == "5":
        print(len(d))
    elif order == "6":
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif order == "7":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif order == "8":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
