import sys

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    primes = [p for p, prime in enumerate(is_prime) if prime]
    return primes

num = sys.stdin.read().splitlines()
for n in num:
    n = int(n)
    if n == 0:
        break
    else:
        primes = sieve_of_eratosthenes(n * 2)
        result = 0
        for i in reversed(primes):
            if i <= 2 * n and i > n:
                result += 1
            if i < n:
                break
        print(result)