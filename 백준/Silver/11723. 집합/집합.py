import sys

S = set()

n = int(sys.stdin.readline())
for _ in range(n):
    orderlist = sys.stdin.readline().split()
    if len(orderlist) == 2:
        order, num = orderlist[0], int(orderlist[1])
        if order == 'add':
            S.add(num)
        elif order == 'remove':
            try:
                S.remove(num)
            except:
                pass
        elif order == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)
        elif order == 'check':
            if num in S:
                print(1)
            else:
                print(0)
    else:
        order = orderlist[0]
        if order == 'all':
            S.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        elif order == 'empty':
            S = set()
