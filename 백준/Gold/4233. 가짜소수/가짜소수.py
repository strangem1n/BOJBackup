import sys, math
input = sys.stdin.readline

def find_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def divide_conquer(n, m):
    global p
    if m <= 1:
        return (n ** m) % p

    temp = divide_conquer(n, m//2)
    if m % 2 == 0:
        return (temp ** 2) % p
    else:
        return ((temp ** 2) * n) % p

memo = set()
while True:
    p, a = map(int, input().split())
    if p == a == 0:
        break

    if p in memo:
        pass
    else:
        if find_prime(p):
            print("no")
            continue
        else:
            memo.add(p)

    if divide_conquer(a, p) == a:
        print("yes")
    else:
        print("no")
