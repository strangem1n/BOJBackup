import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int, input().split()))
time = list(map(int, input().split()))

ans = house[-1]
ans += max(0, time[-1]-house[-1])
for i in range(n-2, -1, -1):
    ans += house[i+1]-house[i]
    if ans < time[i]:
        ans = time[i]
ans += house[0]
print(ans)
