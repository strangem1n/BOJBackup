import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
students = [input().rstrip() for _ in range(n)]

idx = -1
while -idx < len(students[0]):
    chk = defaultdict(bool)
    for s in students:
        if not chk[s[idx:]]:
            chk[s[idx:]] = True
        else:
            idx -= 1
            break
    else:
        break
print(-idx)
    