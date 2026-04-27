star = int(input())
for i in range(star):
    print(" " * (star - 1 - i) + "*" * (2 * i + 1))
for i in range(star-1):
    print(" " * (1 + i) + ("*" * (2 * (star - 1 - i) - 1)))
