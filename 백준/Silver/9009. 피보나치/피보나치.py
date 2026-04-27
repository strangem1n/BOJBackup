import sys
input = sys.stdin.readline

fib = [1, 2]
t = int(input())
for _ in range(t):
    n = int(input())
    while n > fib[-1]:
        fib.append(fib[-1] + fib[-2])
    ans = []
    while n > 0:
        for i in range(len(fib)):
            if fib[-(1+i)] <= n:
                ans.append(fib[-(1+i)])
                n -= fib[-(i+1)]
    for i in range(len(ans)):
        print(ans[-(1+i)], end=" ")
    print("")
