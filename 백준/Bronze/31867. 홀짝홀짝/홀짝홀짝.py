import sys
input = sys.stdin.readline

n = int(input())
num = input().rstrip()
odd = even = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
if odd > even:
    print(1)
elif odd < even:
    print(0)
else:
    print(-1)