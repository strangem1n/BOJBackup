import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(list(range(1, n+1)))

idx = 0
cnt = 0
while idx < m:
    num = q.popleft()
    if num != arr[idx]:
        q.appendleft(num)
        left_q = deepcopy(q)
        right_q = deepcopy(q)
        while True:
            cnt += 1
            left_q.rotate()
            right_q.rotate(-1)
            left = left_q.popleft()
            right = right_q.popleft()
            if left == arr[idx]:
                q = left_q
                break
            elif right == arr[idx]:
                q = right_q
                break
            left_q.appendleft(left)
            right_q.appendleft(right)
    idx += 1
print(cnt)
