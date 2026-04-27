import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = right = cnt = 0
save = float('inf')
while right < n:
    if arr[right] == 1:
        left = right
        break
    else:
        right += 1

if k == 1:
    if right == n:
        print(-1)
    else:
        print(1)
else:
    while right < n:
        if arr[right] == 1:
            cnt += 1
        if cnt < k:
            right += 1
        else:
            save = min(save, right - left)
            while left < right:
                left += 1
                if arr[left] == 1:
                    cnt -= 1
                if cnt < k:
                    right += 1
                    break

    if save == float('inf'):
        print(-1)
    else:
        print(save+1)
