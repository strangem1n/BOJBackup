import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()), reverse=True)

result = 0
last_odd = 0
cnt = 0
for candy in arr:
    if candy % 2 == 0:
        result += candy
    else:
        if cnt == 0:
            cnt += 1
            last_odd = candy
        else:
            cnt -= 1
        result += candy

if cnt == 1:
    result -= last_odd
print(result)