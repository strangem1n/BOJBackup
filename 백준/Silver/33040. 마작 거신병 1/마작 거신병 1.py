import sys
input = sys.stdin.readline

h, w = map(int, input().split())
c, d = map(int, input().split())

arr = [0] * h
idx = 0
chk = True
nine = d

if h > 1 and nine < h * (h-1) // 2:
    chk = False
else:
    while nine > 0:
        if idx < h:
            idx += 1
        for i in range(1, idx+1):
            arr[-i] += 1
            nine -= 1
            if arr[-i] > w:
                chk = False
                break
            if nine == 0:
                break
        if not chk:
            break

if chk:
    for i in arr:
        for _ in range(i):
            print("9", end=" ")
        for _ in range(w-i):
            print("1", end=" ")
        print("")
else:
    print(-1)
