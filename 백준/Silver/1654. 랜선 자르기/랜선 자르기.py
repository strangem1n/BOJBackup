import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for _ in range(k):
    lan = int(input())
    arr.append(lan)

start = 1
end = max(arr)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for lan in arr:
        total += lan // mid
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
