n, m = map(int, input().split())
buckets = []
for i in range(1, n+1):
    buckets.append(i)

for _ in range(m):
    i, j = map(int, input().split())
    buckets_div1 = buckets[:i-1]
    buckets_div2 = buckets[i-1:j]
    buckets_div3 = buckets[j:]
    buckets_div2.reverse()
    buckets = buckets_div1 + buckets_div2 + buckets_div3

print(*buckets)
