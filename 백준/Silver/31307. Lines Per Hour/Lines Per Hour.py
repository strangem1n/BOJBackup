n, m = map(int, input().split())
problem = [int(input()) for _ in range(n)]
problem.sort()

m *= 5
cnt = 0
for p in problem:
    m -= p
    if m >= 0:
        cnt += 1
    else:
        break
print(cnt)