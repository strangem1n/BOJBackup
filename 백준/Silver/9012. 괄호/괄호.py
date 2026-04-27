n = int(input())
for _ in range(n):
    vpschk = input()
    i = 0
    while True:
        try:
            if vpschk[i] == '(' and vpschk[i+1] == ')':
                vpschk = vpschk[:i] + vpschk[i+2:]
                i = 0
            else:
                i += 1
        except IndexError:
            break
    if vpschk == '':
        print('YES')
    else:
        print('NO')