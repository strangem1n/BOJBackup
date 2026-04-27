import sys
a, b = map(int, sys.stdin.readline().split())

cnt = num = result = 0
while cnt <= b:
    num += 1
    for n in range(1, num+1):
        cnt += 1
        if a <= cnt <= b:
            result += num
print(result)