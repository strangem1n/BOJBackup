import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

stack = [[1, 0]]
visited = [False] * (n+1)
visited[1] = True
ans = 0
while stack:
    parent, depth = stack.pop()
    chk = False
    for child in adj[parent]:
        if not visited[child]:
            chk = True
            visited[child] = True
            stack.append([child, depth+1])
    if not chk and len(adj[parent]) == 1:
            ans += depth
if ans % 2 == 0:
    print("No")
else:
    print("Yes")
