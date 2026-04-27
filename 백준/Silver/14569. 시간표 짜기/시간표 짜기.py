import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
sub = defaultdict(list)
for _ in range(n):
    t, *num = map(int, input().split())
    sub[t].append(num)

m = int(input())
for _ in range(m):
    ti, *rest = map(int, input().split())
    result = 0
    for i in range(ti, 3, -1):
        for subject in sub[i]:
            chk = set(subject)
            if chk == chk & set(rest):
                result += 1
    print(result)
