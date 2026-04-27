import sys
input = sys.stdin.readline

fib = [0] * 479
fib[0] = 1
fib[1] = 2
for i in range(2, 479):
    fib[i] = fib[i-1] + fib[i-2]

while True:
    a, b = map(int, input().split())
    cnt = 0
    if a == b == 0:
        break
    for i in range(479):
        if fib[i] < a:
            continue
        if fib[i] <= b:
            cnt += 1
        else:
            break
    print(cnt)