a = int(input())
for _ in range(a):
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor = str(h)
        num = str(n // h)
        if len(num) < 2:
            num = '0' + num
        print(floor + num)
    else:
        floor = str(n % h)
        num = str(n // h + 1)
        if len(num) < 2:
            num = '0' + num
        print(floor + num)