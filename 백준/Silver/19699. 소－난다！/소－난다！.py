import sys
from itertools import combinations
import math
input = sys.stdin.readline

def prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

n, m = map(int, input().split())
c = sorted(map(int, input().split()))
cow = combinations(c, m)
result = set()
for ci in cow:
    s = sum(ci)
    if prime(s):
        result.add(s)
if len(result) == 0:
    print(-1)
else:
    print(*sorted(result))
