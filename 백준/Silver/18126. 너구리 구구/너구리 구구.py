import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited[1] = 1
    q = deque([1])

    while q:
        node = q.popleft()
        for next_node, next_cost in adj[node]:
            if visited[next_node] == 0:
                visited[next_node] = visited[node] + next_cost
                q.append(next_node)

    return max(visited) - 1


n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
visited = [0] * (n+1)
result = bfs()
print(result)