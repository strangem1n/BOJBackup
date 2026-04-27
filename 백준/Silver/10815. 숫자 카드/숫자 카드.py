import sys

card = int(sys.stdin.readline())
cardnum = set(map(int, sys.stdin.readline().split()))
check = int(sys.stdin.readline())
checknum = list(map(int, sys.stdin.readline().split()))

for i in checknum:
    if i in cardnum:
        print(1, end=" ")
    else:
        print(0, end=" ")