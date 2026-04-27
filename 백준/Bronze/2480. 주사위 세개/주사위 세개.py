a, b, c = map(int, input().split())
if a == b == c:
    print ("%d" % (a * 1000 + 10000))
elif a == b or a == c:
    print ("%d" % (a * 100 + 1000))
elif b == c:
    print ("%d" % (b * 100 + 1000))
else:
    if a > b and a > c:
        print ("%d" % (a * 100))
    elif b > a and b > c:
        print ("%d" % (b * 100))
    else:
        print ("%d" % (c * 100))