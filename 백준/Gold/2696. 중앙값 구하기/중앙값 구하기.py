import sys, math, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    print(math.ceil(n/2))
    arr = []
    for i in range(math.ceil(n/10)):
        arr.extend(list(map(int, input().split())))
    center = arr[0]
    print(center, end=' ')
    left = []
    right = []

    left_cnt = right_cnt = 0
    for i in range(1, n):
        if arr[i] > center:
            heapq.heappush(right, arr[i])
            right_cnt += 1
        else:
            heapq.heappush(left, -arr[i])
            left_cnt += 1

        if i % 20 == 0:
            print('')

        if i % 2 == 0:
            if left_cnt < right_cnt:
                heapq.heappush(left, -center)
                center = heapq.heappop(right)
                print(center, end=' ')
            elif left_cnt > right_cnt:
                heapq.heappush(right, center)
                center = -heapq.heappop(left)
                print(center, end=' ')
            else:
                print(center, end=' ')
            left_cnt = right_cnt = 0

    if n % 20 != 0:
        print('')
