n = int((input()))
info = []
for _ in range(n):
    a, b = input().split()
    a = int(a)
    info.append([a, b])
info.sort(key=lambda x:x[0])
for i in info:
    print(*i)