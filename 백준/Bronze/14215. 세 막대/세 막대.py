tri = list(map(int, input().split()))

c = max(tri)
tri.remove(c)
a = min(tri)
tri.remove(a)
b = tri[0]

if a + b <= c:
    c = (a + b - 1)

print(a+b+c)