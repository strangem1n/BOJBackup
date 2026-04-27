import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = sum(arr) // n
diff = deque([arr[i]-m for i in range(n)])
dis = 0
for _ in range(n*2):
    if diff[0] > 0:
        dis += diff[0]
        diff[1] += diff[0]
        diff[0] = 0
    diff.rotate(-1)
print(dis)
