while True:
    checker = True
    n = str(input())
    if n == '0':
        break
    for i in range((len(n)//2)+1):
        if n[i] == n[-1-i]:
            continue
        else:
            checker = False
            break
    if checker is True:
        print('yes')
    else:
        print('no')