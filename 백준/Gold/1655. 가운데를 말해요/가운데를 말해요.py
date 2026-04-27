import sys, heapq
input = sys.stdin.readline

n = int(input())
min_q = []
max_q = []
idx = 0
mid = int(input())
print(mid)
for i in range(n-1):
    num = int(input())

    if not max_q:
        if num > mid:
            heapq.heappush(max_q, num)
        else:
            heapq.heappush(max_q, mid)
            mid = num
        idx += 1
    else:
        if num > mid:
            heapq.heappush(max_q, num)
            idx += 1
        else:
            heapq.heappush(min_q, -num)
            idx -= 1

    if i % 2 == 0:
        if idx > 0:
            temp = heapq.heappop(max_q)
            if mid > temp:
                heapq.heappush(max_q, mid)
                mid = temp
            else:
                heapq.heappush(max_q, temp)
            print(mid)
        else:
            temp = -heapq.heappop(min_q)
            if mid < temp:
                print(mid)
                heapq.heappush(min_q, -mid)
                mid = temp
            else:
                print(temp)
                heapq.heappush(min_q, -temp)
    else:
        if idx == 2:
            heapq.heappush(min_q, -mid)
            mid = heapq.heappop(max_q)
            idx = 0
        elif idx == -2:
            heapq.heappush(max_q, mid)
            mid = -heapq.heappop(min_q)
            idx = 0
        print(mid)
