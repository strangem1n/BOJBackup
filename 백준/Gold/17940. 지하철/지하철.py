import sys, heapq
input = sys.stdin.readline

def solve():
    pq = []
    dist = [float("inf")] * n
    heapq.heappush(pq, [0, 0, 0, company[0]])
    while pq:
        t, d, v, c = heapq.heappop(pq)
        if v == m:
            return t, d
        dist[v] = d
        for i in range(n):
            next_d = adj[v][i]
            if next_d == 0:
                continue
            elif d + next_d > dist[i]:
                continue
            else:
                dist[i] = d + next_d
                next_t = 0
                if c != company[i]:
                    next_t += 1
                heapq.heappush(pq, [t+next_t, d+next_d, i, company[i]])

n, m = map(int, input().split())
company = [int(input()) for _ in range(n)]
adj = [list(map(int, input().split())) for _ in range(n)]
print(*solve())
