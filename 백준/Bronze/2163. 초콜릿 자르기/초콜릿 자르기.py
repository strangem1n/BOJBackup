import sys
def divide(x, y):
    if x == 1:
        if y == 1:
            return 0
        else:
            return 1 + divide(x, y//2) + divide(x, y-(y//2))
    else:
        return 1 + divide(x//2, y) + divide(x-(x//2), y)
print(divide(*map(int, sys.stdin.readline().split())))
