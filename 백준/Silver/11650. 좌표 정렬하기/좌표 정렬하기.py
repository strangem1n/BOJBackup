n = int((input()))
pos = []
zero = []
neg = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] > 0:
        pos.append(a)
    elif a[0] == 0:
        zero.append(a)
    else:
        neg.append(a)

neg.sort()
for i in neg:
    print(*i)
zero.sort()
for i in zero:
    print(*i)
pos.sort()
for i in pos:
    print(*i)