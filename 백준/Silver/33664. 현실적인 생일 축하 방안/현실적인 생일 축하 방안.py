import sys
input = sys.stdin.readline

b, n, m = map(int, input().split())
store = {}
for _ in range(n):
    i, p = input().split()
    store[i] = int(p)
budget = 0
for _ in range(m):
    j = input().rstrip()
    budget += store[j]
if budget > b:
    print('unacceptable')
else:
    print('acceptable')
