import sys
input = sys.stdin.readline
x = input().rstrip()
ans = [False] * 5
for i in x:
    if i == 'M':
        ans[0] = True
    elif i == 'O':
        ans[1] = True
    elif i == 'B':
        ans[2] = True
    elif i == 'I':
        ans[3] = True
    elif i == 'S':
        ans[4] = True
for a in ans:
    if not a:
        print('NO')
        break
else:
    print('YES')
