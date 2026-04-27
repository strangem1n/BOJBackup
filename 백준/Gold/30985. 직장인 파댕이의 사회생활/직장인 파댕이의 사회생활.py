import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def solve():
    first_floor = dijk(1)
    for i in range(n):
        if e[i] == -1:
            first_floor[i+1] = INF
        else:
            first_floor[i+1] += e[i] * (k-1)
    top_floor = dijk(n)
    min_result = INF
    for i in range(1, n+1):
        result = first_floor[i] + top_floor[i]
        if min_result > result:
            min_result = result
    if min_result == INF:
        return -1
    else:
        return min_result

def dijk(start):
    pq = [[0, start]]
    dist = [INF] * (n+1)
    while pq:
        cost, room = heapq.heappop(pq)
        if dist[room] < cost:
            continue
        dist[room] = cost
        for next_cost, next_room in adj[room]:
            final_cost = cost + next_cost
            if dist[next_room] <= final_cost:
                continue
            dist[next_room] = final_cost
            heapq.heappush(pq, [final_cost, next_room])
    return dist

n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, c = map(int, input().split())
    adj[u].append([c, v])
    adj[v].append([c, u])
e = list(map(int, input().split()))
print(solve())
