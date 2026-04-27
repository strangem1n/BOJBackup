n, m = map(int, input().split())
buckets = {}

for p in range(1, n+1):
    buckets[p] = p

for _ in range(m):
    i, j = map(int, input().split())
    buckets[i], buckets[j] = buckets[j], buckets[i]

result = buckets.values()
print(*result)