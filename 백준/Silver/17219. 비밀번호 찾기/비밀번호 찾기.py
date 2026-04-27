n, m = map(int, input().split())
memo = {}
for _ in range(n):
    a, b = input().split()
    memo[a] = b
for _ in range(m):
    c = input()
    print(memo.get(c))