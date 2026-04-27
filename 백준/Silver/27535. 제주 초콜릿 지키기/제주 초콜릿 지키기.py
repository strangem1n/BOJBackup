import sys
input = sys.stdin.readline

def count_choco(n, d):
    result = "7H"
    while n > 0:
        result = str(n % d) + result
        n //= d
    return result

chocolate = list(map(lambda x: [int(x), ""], input().split()))
chocolate[0][1] = "H"
chocolate[1][1] = "T"
chocolate[2][1] = "C"
chocolate[3][1] = "K"
chocolate[4][1] = "G"

m = int(input())
for _ in range(m):
    all_choco = 0
    for i in range(5):
        all_choco += chocolate[i][0]
    div = int(str(all_choco)[-1])
    div = 10 if div == 0 or div == 1 else div

    hi, ti, ci, ki, gi = map(int, input().split())
    chocolate[0][0] -= hi
    chocolate[1][0] -= ti
    chocolate[2][0] -= ci
    chocolate[3][0] -= ki
    chocolate[4][0] -= gi

    all_choco = 0
    for i in range(5):
        all_choco += chocolate[i][0]
    sort_choco = sorted(chocolate, key=lambda x: (-x[0], x[1]))

    if all_choco > 0:
        print(count_choco(all_choco, div))
        for left_choco, flavor in sort_choco:
            if left_choco == 0:
                break
            print(flavor, end="")
        print("")
    else:
        print("07H")
        print("NULL")
