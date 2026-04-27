import sys
a, b = map(int, sys.stdin.readline().split())
ai = a%4
if ai == 0:
    ai = 4
bi = b%4
if bi == 0:
    bi = 4
aj = a//4
bj = b//4
if ai == 4:
    aj -= 1
if bi == 4:
    bj -= 1
w = abs(aj-bj)
h = abs(ai-bi)
print(w+h)