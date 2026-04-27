a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
n = []

if a == c:
    n.append(e)
elif a == e:
    n.append(c)
elif c == e:
    n.append(a)

if b == d:
    n.append(f)
elif b == f:
    n.append(d)
elif d == f:
    n.append(b)

print(*n)