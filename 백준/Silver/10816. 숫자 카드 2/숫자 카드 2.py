import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
card = {}
for i in num:
    if i in card:
        card[i] += 1
    else:
        card[i] = 1
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
for i in check:
    print(card.get(i, 0), end=" ")