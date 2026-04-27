import sys
input = sys.stdin.readline

n, m = map(int, input().split())
com = [False] * n
cnt = n
for _ in range(m):
    q = input().rstrip()
    if q == "3":
        print(cnt)
    else:
        i, j = map(int, q.split())
        j -= 1
        if i == 1:
            if not com[j]:
                cnt -= 1
                com[j] = True
        else:
            if com[j]:
                cnt += 1
                com[j] = False
