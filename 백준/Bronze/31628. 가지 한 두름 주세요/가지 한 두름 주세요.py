import sys
input = sys.stdin.readline

def solve():
    for i in range(10):
        temp1 = arr[i][0]
        temp2 = arr[0][i]
        chk1 = chk2 = True
        for j in range(1, 10):
            if chk1:
                if temp1 != arr[i][j]:
                    chk1 = False
            if chk2:
                if temp2 != arr[j][i]:
                    chk2 = False
            if not chk1 and not chk2:
                break
        else:
            return 1
    return 0

arr = [list(input().split()) for _ in range(10)]
print(solve())