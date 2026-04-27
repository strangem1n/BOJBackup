import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    if t >= arr[i]:
        t -= arr[i]
    else:
        print(i)
        break
else:
    print(n)
