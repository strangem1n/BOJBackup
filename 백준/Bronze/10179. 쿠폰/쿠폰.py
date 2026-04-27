import sys
input = sys.stdin.readline

def discount(price):
    return price * 0.8

t = int(input())
for _ in range(t):
    n = float(input())
    print(f"${discount(n):.2f}")
