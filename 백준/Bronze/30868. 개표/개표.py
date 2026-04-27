import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    print("++++ " * (n // 5), end="")
    print("|" * (n % 5), end="")
    print("\n", end="")