n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    arr = list(map(int, input().split()))
    box = 0
    result = 1
    for book in arr:
        if box + book <= m:
            box += book
        else:
            result += 1
            box = 0
            box += book
    print(result)