import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = sorted(map(int, input().split()))
c = []
for idx, m in enumerate(a):
    c.append([m, idx])
c.sort(key=lambda x: x[0])
for i in range(n):
    if c[i][0] > b[i]:
        print(-1)
        break
    else:
        c[i][0] = b[i]
else:
    c.sort(key=lambda x: x[1])
    for k, _ in c:
        print(k, end=" ")
