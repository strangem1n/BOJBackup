import sys
input = sys.stdin.readline

def solve(n):
    ans = 1
    while n > 9:
        for i in range(9, 1, -1):
            if n % i == 0:
                ans += 1
                n //= i
                break
        else:
            return -1
    return ans

t = int(input())
for _ in range(t):
    num = int(input())
    print(solve(num))
