import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

sum_n = []
sum_m = []
for i in range(n):
    sum_n.append(sum(arr[i]))
for j in range(m):
    s = 0
    for i in range(n):
        s += arr[i][j]
    sum_m.append(s)

ans = -float("inf")
for i in range(n):
    for j in range(i+1, n):
        for k in range(m):
            for l in range(k+1, m):
                s = sum_n[i]+sum_n[j]+sum_m[k]+sum_m[l]-(arr[i][k]+arr[j][k]+arr[i][l]+arr[j][l])+((j-1-i)*(l-1-k))
                if ans < s:
                    ans = s
print(ans)
