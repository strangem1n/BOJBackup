import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n+1):
    adj[i].sort()

q = deque([r])
visited[r] = cnt = 1
while q:
    node = q.popleft()
    for next_node in adj[node]:
        if not visited[next_node]:
            cnt += 1
            visited[next_node] = cnt
            q.append(next_node)

for i in range(1, n+1):
    print(visited[i])