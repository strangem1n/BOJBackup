import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = sum(arr[:k])
ans = s
left = 0
right = k-1
while right < n-1:
    right += 1
    s += arr[right]
    s -= arr[left]
    left += 1
    if ans < s:
        ans = s
print(ans)
