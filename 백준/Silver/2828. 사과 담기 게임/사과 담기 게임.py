n, m = map(int, input().split())
j = int(input())
apple = [int(input()) for _ in range(j)]

start = 1
end = 1 + m - 1

cnt = 0
for a in apple:
    if end < a:
        move = a - end
        cnt += move
        start += move
        end += move
    elif start > a:
        move = start - a
        cnt += move
        start -= move
        end -= move
print(cnt)