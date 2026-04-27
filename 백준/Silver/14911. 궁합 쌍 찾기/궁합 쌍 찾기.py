import sys
from collections import defaultdict
input = sys.stdin.readline

arr = sorted(map(int, input().split()))
num = int(input())
memo = defaultdict(bool)

cnt = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == num and not memo[(arr[i], arr[j])]:
            print(arr[i], arr[j])
            memo[(arr[i], arr[j])] = True
            cnt += 1
print(cnt)
