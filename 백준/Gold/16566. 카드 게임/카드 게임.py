import sys
from bisect import bisect_right
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        x, y = y, x
    parent[x] = y

n, m, k = map(int, input().split())
card = sorted(map(int, input().split()))
parent = list(range(m+1))
cheolsoo = map(int, input().split())

for c in cheolsoo:
    idx = find(bisect_right(card, c))
    print(card[idx])
    union(idx, idx+1)
