import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = input().rstrip()
    r = n[::-1]
    chk = str(int(n) + int(r))
    for i in range(len(chk)):
        if chk[i] != chk[-(i+1)]:
            print("NO")
            break
    else:
        print("YES")