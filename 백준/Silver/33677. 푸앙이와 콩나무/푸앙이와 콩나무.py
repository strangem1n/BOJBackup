import sys
from collections import deque

def solve(k):
    q = deque([(0, 0, 0)])
    visited = [float('inf')] * (k+1)
    while True:
        nq = deque([])
        while q:
            day, length, water = q.popleft()
            if water >= visited[length]:
                continue
            visited[length] = water
            if 1 < length < int(k**(1/2))+1:
                nq.append((day+1, length**2, water+5))
            if 0 < length < k//3+1:
                nq.append((day+1, length*3, water+3))
            if length < k:
                nq.append((day+1, length+1, water+1))
        if visited[k] == float('inf'):
            q = nq
        else:
            return day, visited[k]

n = int(sys.stdin.readline())
print(*solve(n))
