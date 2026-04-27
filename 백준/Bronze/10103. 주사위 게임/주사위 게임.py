import sys
input = sys.stdin.readline

c = s = 100
t = int(input())
for _ in range(t):
    c1, s1 = map(int, input().split())
    if c1 > s1:
        s -= c1
    elif c1 < s1:
        c -= s1
print(c)
print(s)