def worm(n, a):
    stack = [0] * (n+1)
    visit = [0] * (n+1)
    top = 0
    start = 1
    stack[top] = start
    infected = 0
    while top >= 0:
        visit[start] = 1
        for j in range(len(a[start])):
            end = a[start][j]
            if visit[end] == 0:
                stack[top] = start
                top += 1
                infected += 1
                start = end
                break
        else:
            top -= 1
            start = stack[top]
    return infected

import sys
input = sys.stdin.readline

n = int(input())
pair = int(input())
adj_list = [list(map(int, input().split())) for _ in range(pair)]
adj = [[] for _ in range(n+1)]
for i in range(pair):
    v, w = adj_list[i]
    adj[v].append(w)
    adj[w].append(v)
result = worm(n, adj)
print(result)
