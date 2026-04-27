import sys, bisect
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    result = 0
    for ai in a:
        result += bisect.bisect_left(b, ai)
    print(result)
