import sys
input = sys.stdin.readline

n = int(input())
ab = input().rstrip()
a = b = 0
for i in ab:
    if i == "A":
        a += 1
    else:
        b += 1
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")
