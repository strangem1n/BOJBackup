import sys
from collections import defaultdict

def solve():
    dic = defaultdict(bool)
    cnt = chk = 0
    while True:
        cnt += 1
        for i in range(n-(cnt-1)):
            num = ""
            for j in range(cnt):
                num += arr[i+j]
            dic[int(num)] = True

        while chk < 10 ** cnt:
            if not dic[chk]:
                return chk
            else:
                chk += 1

n = int(sys.stdin.readline())
d = sys.stdin.read().splitlines()
arr = []
for di in d:
    arr.extend(di.split())
print(solve())
