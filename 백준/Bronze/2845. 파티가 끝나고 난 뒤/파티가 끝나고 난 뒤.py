n, m = map(int, input().split())
arr = list(map(lambda x: int(x)-n*m, input().split()))
print(*arr)