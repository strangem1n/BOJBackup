t = int(input())
for tc in range(1, t+1):
    s, b = map(int, input().split())
    print(f"Practice #{tc}: {s} {b}")
    m = int(input())
    for _ in range(m):
        g = int(input())
        while b <= g:
            b *= 2
        b -= g
        print(g, b)
    print('')
