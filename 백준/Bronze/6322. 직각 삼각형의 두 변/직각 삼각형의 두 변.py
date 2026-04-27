import sys, math
input = sys.stdin.readline

t = 0
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    t += 1
    print(f"Triangle #{t}")
    try:
        if a == -1:
            na = math.sqrt(c**2-b**2)
            if na == 0:
                raise ValueError
            print(f"a = {na:.3f}")
        elif b == -1:
            nb = math.sqrt(c**2-a**2)
            if nb == 0:
                raise ValueError
            print(f"b = {nb:.3f}")
        else:
            nc = math.sqrt(a**2+b**2)
            if nc == 0:
                raise ValueError
            print(f"c = {nc:.3f}")
    except ValueError:
        print("Impossible.")
    finally:
        print("")
