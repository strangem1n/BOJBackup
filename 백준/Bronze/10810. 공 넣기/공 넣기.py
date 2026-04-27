n, m = map(int, input().split())
buckets = {}

for p in range(1, n+1):
    buckets[p] = 0

for _ in range(m):
    i, j, k = map(int, input().split())
    for q in range(i, j+1):
        buckets[q] = k

result = buckets.values()
print(*result)