import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
q = deque([(1, 0)])
visited = [0] * (n+1)
visited[1] = 1
while q:
    num, re = q.popleft()
    for friend in adj[num]:
        if visited[friend]:
            continue
        visited[friend] = 1
        if re < 1:
            q.append((friend, re+1))
print(sum(visited)-1)
