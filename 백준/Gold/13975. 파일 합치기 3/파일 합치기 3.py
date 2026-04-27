import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    pq = list(map(int, input().split()))
    heapq.heapify(pq)

    result = 0
    while True:
        x = heapq.heappop(pq)
        if not pq:
            break
        y = heapq.heappop(pq)
        result += x+y
        heapq.heappush(pq, x+y)
    print(result)