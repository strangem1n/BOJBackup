import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())
arr = deque(map(int, input().split()))
for _ in range(q):
    t, *text = map(int, input().split())
    if t == 1:
        idx, num = text
        arr[idx-1] += num
    elif t == 2:
        arr.rotate(text[0])
    else:
        arr.rotate(-text[0])
print(*arr)
