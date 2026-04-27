import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

max_cnt = 2
for i in range(n):
    cnt = 2
    for j in range(i, n-2):
        if arr[j] <= arr[j+1] <= arr[j+2]:
            break
        elif arr[j] >= arr[j+1] >= arr[j+2]:
            break
        else:
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)