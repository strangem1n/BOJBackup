import sys
import heapq
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

hq = []
m = float('inf')
for i in range(l):
    heapq.heappush(hq, (arr[i], i))
    if m >= arr[i]:
        m = arr[i]
    print(m, end=" ")

for i in range(l, n):
    left = i-l
    heapq.heappush(hq, (arr[i], i))
    pop, idx = heapq.heappop(hq)
    while idx <= left:
        pop, idx = heapq.heappop(hq)
    print(pop, end=" ")
    heapq.heappush(hq, (pop, idx))
