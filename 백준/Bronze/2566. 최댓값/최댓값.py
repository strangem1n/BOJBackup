N = {}
M = []

for i in range(1, 10):
    n = list(map(int, input().split()))
    m = max(n)
    M.append(m)
    N[i] = n.index(m) + 1

MAX = M.index(max(M)) + 1
loc = N.get(MAX)

print(max(M))
print(MAX, loc)