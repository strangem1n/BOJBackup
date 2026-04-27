import sys
input = sys.stdin.readline

arr = list(input().rstrip())
for a in arr:
    temp = ord(a)
    cnt = 0
    while temp > 9:
        cnt += temp % 10
        temp //= 10
    cnt += temp 
    print(a*cnt)
