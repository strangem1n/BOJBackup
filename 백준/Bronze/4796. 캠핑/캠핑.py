import sys

t = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l == p == v == 0:
        break
    print(f"Case {t}: {v//p*l+min(l, v%p)}")
    t += 1