T = int(input())
for _ in range(T):
    arr = list(map(lambda x: x[::-1], input().split()))
    print(*arr)