import sys
from bisect import bisect_left
input = sys.stdin.readline

n, q = map(int, input().split())
problem = list(map(int, input().split()))

left_lis = [0] * n
lis = []
lis_length = []

for i in range(n):
    pos = bisect_left(lis, problem[i])
    if pos == len(lis):
        lis.append(problem[i])
        lis_length.append(1)
    else:
        lis[pos] = problem[i]
        lis_length[pos] = 1

    left_lis[i] = pos + 1

right_lis = [0] * n
lis = []
lis_length = []

for i in range(n - 1, -1, -1):
    pos = bisect_left(lis, -problem[i])
    if pos == len(lis):
        lis.append(-problem[i])
        lis_length.append(1)
    else:
        lis[pos] = -problem[i]
        lis_length[pos] = 1

    right_lis[i] = pos + 1

for _ in range(q):
    idx = int(input()) - 1
    result = left_lis[idx] + right_lis[idx] - 1
    print(result)