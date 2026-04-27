import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a = sum(map(int, input().split()))
if t > a:
    print("Padaeng_i Cry")
else:
    print("Padaeng_i Happy")
