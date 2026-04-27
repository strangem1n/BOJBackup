import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.append(0)
cnt = max_length = 0
length = 1
for i in range(n):
    if arr[i] <= arr[i+1]:
        length += 1
    else:
        cnt += 1
        if max_length < length:
            max_length = length
        length = 1
print(cnt, max_length)
