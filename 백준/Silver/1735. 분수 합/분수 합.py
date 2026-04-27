import sys, math
a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())
b3 = math.lcm(b1,b2)
a3 = int((a1 * b3 / b1) + (a2 * b3 / b2))
gcd = int(math.gcd(a3,b3))
if math.gcd(a3,b3) != 1:
    a3 = a3 / gcd
    b3 = b3 / gcd
print(int(a3), int(b3))
