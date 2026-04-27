import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
city = [False] * (n+1)
power_station = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append([w, v])
    adj[v].append([w, u])

cnt = len(power_station)
pq = []
for p in power_station:
    city[p] = True
    for cost, adj_city in adj[p]:
        heapq.heappush(pq, [cost, adj_city])

total_cost = 0
while pq and cnt < n:
    cost, adj_city = heapq.heappop(pq)
    if not city[adj_city]:
        city[adj_city] = True
        cnt += 1
        total_cost += cost
        for next_cost, next_city in adj[adj_city]:
            if not city[next_city]:
                heapq.heappush(pq, [next_cost, next_city])
print(total_cost)
