import sys
input = sys.stdin.readline

def find(x):
    while pa[x] != x:
        return find(pa[x])
    return x

def union(x, y):
    if find(x) > find(y):
        x, y = y, x
    pa[find(y)] = find(x)

def solve(x, y):
    if find(x) == find(y):
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    k = int(input())
    pa = [i for i in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    m = int(input())
    print(f"Scenario {tc}:")
    for _ in range(m):
        u, v = map(int, input().split())
        print(solve(u, v))
    print("")
