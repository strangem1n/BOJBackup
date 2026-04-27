n, k = map(int, input().split())
k1 = n - k
k = min(k, k1)
N = 1
K = 1
for i in range(k):
    N *= (n - i)
    K *= (i + 1)
print(int(N/K))