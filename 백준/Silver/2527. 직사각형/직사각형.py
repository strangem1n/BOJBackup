for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:    # 공통부분이 없음
        print('d')
    elif (p1, y1) == (x2, q2) or (p1, q1) == (x2, y2) or (x1, q1) == (p2, y2) or (x1, y1) == (p2, q2):    # 한 점에서 만남
        print('c')
    elif y1 == q2 or p1 == x2 or q1 == y2 or p2 == x1:    # 선분으로 만남
        print('b')
    else:    # 직사각형으로 겹침
        print('a')
