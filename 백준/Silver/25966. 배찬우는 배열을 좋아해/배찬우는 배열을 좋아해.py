import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
query = {}

for x in range(n):
    data = list(map(int, input().split()))
    query[x] = data

for _ in range(q):
    order = list(map(int, input().split()))
    i = order[1]
    j = order[2]
    if order[0] == 0:
        k = order[3]
        query[i][j] = k
    else:
        query[i], query[j] = query[j], query[i]

for x in range(n):
    print(*query[x])