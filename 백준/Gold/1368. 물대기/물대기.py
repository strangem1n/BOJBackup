import sys, heapq
input = sys.stdin.readline

n = int(input())
pq = [[int(input()), i] for i in range(n)]
adj = [list(map(int, input().split())) for _ in range(n)]
heapq.heapify(pq)

is_water = [False] * n
total_cost = 0
init_cost, init_field = heapq.heappop(pq)
total_cost += init_cost
is_water[init_field] = True
for i in range(n):
    if i == init_field:
        continue
    heapq.heappush(pq, [adj[init_field][i], i])
cnt = 1
while pq and cnt < n:
    cost, field = heapq.heappop(pq)
    if not is_water[field]:
        cnt += 1
        is_water[field] = True
        total_cost += cost
        for i in range(n):
            if is_water[i]:
                continue
            heapq.heappush(pq, [adj[field][i], i])
print(total_cost)
