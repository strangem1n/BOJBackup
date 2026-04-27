import sys
n, m = map(int, sys.stdin.readline().split())
hear = set()
for _ in range(n):
    hear.add(sys.stdin.readline().rstrip())
see = set()
for _ in range(m):
    see.add(sys.stdin.readline().rstrip())
worst = hear & see
worst = list(worst)
worst.sort()
print(len(worst))
for i in worst:
    print(i)