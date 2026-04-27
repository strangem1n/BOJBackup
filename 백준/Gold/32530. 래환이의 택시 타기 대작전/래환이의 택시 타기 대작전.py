import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (60 * 24)
for _ in range(n):
    h, m = map(int, input().split(":"))
    arr[h*60+m] += 1
ans = 0
for i in range(60*24):
    while arr[i] > 0:
        ans += 1
        cnt = 3
        for j in range(21):
            while i+j < 60*24 and arr[i+j] > 0:
                arr[i+j] -= 1
                cnt -= 1
                if cnt == 0:
                    break
            if cnt == 0:
                break
print(ans)
