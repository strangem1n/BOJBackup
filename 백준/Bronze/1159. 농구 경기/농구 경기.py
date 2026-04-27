import sys
input = sys.stdin.readline

arr = [0] * 26
n = int(input())
for _ in range(n):
    arr[ord(input()[0])-97] += 1
chk = False
for i in range(26):
    if arr[i] >= 5:
        print(chr(i+97), end="")
        chk = True
if not chk:
    print("PREDAJA")
