x, y, w, h = map(int, input().split())
a = abs(x - w)
b = x - 0
c = abs(y - h)
d = y - 0
n = [a, b, c, d]
print(min(n))