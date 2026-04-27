import sys
input = sys.stdin.readline

n = int(input())
magnet = input().rstrip()
chk = magnet[:2]

for i in range(0, n*2, 2):
    if chk != magnet[i:i+2]:
        print("No")
        break
else:
    print("Yes")