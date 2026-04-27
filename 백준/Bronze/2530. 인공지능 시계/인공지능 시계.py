import sys
input = sys.stdin.readline
h, m, s = map(int, input().split())
add = int(input())
s += add
if s >= 60:
    m += s // 60
    s = s % 60
if m >= 60:
    h += m // 60
    m = m % 60
if h >= 24:
    h = h % 24
print(h, m, s)