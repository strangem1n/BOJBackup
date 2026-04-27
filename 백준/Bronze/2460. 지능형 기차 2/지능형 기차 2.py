import sys

max_train = train = 0
for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())
    train -= a
    train += b
    max_train = max(max_train, train)
print(max_train)
