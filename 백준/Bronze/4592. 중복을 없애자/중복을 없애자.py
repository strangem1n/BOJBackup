import sys
input = sys.stdin.readline
while True:
    n, *arr = map(int, input().split())
    if n == 0:
        break
    ans = []
    for a in arr:
        if ans and ans[-1] == a:
            continue
        ans.append(a)
    ans.append("$")
    print(*ans)