import sys
input = sys.stdin.readline

n, k = map(int, input().split())
school = [[0, 0] for _ in range(7)]
for _ in range(n):
    s, y = map(int, input().split())
    school[y][s] += 1
ans = 0
for m, f in school:
    ans += m // k
    if m % k > 0:
        ans += 1
    ans += f // k
    if f % k > 0:
        ans += 1
print(ans)