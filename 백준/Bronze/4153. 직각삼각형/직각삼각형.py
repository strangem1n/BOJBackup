def Triangle(a, b, max):
    if max ** 2 == a ** 2 + b ** 2:
        print('right')
    else:
        print('wrong')
    return

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    h = max(a, b, c)
    if h == a:
        Triangle(b, c, h)
    elif h == b:
        Triangle(a, c, h)
    else:
        Triangle(a, b, h)