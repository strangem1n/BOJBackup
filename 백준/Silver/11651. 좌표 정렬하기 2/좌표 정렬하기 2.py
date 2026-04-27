n = int((input()))
pos = []
zero = []
neg = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[1] > 0:
        pos.append(a)
    elif a[1] == 0:
        zero.append(a)
    else:
        neg.append(a)

neg.sort(key=lambda x:(x[1], x[0]))
for i in neg:
    print(*i)
zero.sort(key=lambda x:x[0])
for i in zero:
    print(*i)
pos.sort(key=lambda x:(x[1], x[0]))
for i in pos:
    print(*i)