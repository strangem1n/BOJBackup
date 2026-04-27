import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    p = input().rstrip()
    if p == 'P=NP':
        print('skipped')
    else:
        print(sum(map(int, p.split('+'))))