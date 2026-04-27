import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    heapq.heappush(adj[u], v)
    heapq.heappush(adj[v], u)
stack = [r]
visited = [0] * (n+1)
idx = 1
while stack:
    node = stack[-1]
    if not visited[node]:
        visited[node] = idx
        idx += 1
    while adj[node]:
        new_node = heapq.heappop(adj[node])
        if not visited[new_node]:
            stack.append(new_node)
            break
    else:
        stack.pop()
for i in range(1, n+1):
    print(visited[i])
