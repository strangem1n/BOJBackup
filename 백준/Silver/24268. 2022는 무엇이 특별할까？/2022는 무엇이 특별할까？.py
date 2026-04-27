import sys
from itertools import permutations
input = sys.stdin.readline

def solve(n, d):
    res = ""
    while n >= d:
        res = str(n%d) + res
        n //= d
    if n:
        res = str(n) + res

    if len(res) > d:
        return -1

    for p in permutations([i for i in range(d)]):
        next_res = "".join(map(str, p))
        if int(next_res) > int(res):
            if next_res[0] == "0":
                continue
            ans = 0
            for k in range(len(next_res)):
                ans += int(next_res[-(k+1)]) * (d ** k)
            return ans
    return -1

num, deg = map(int, input().split())
print(solve(num, deg))
