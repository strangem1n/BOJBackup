n = int(input())
board = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
for i in range(m):
    if check[i] in board:
        print(1)
    else:
        print(0)