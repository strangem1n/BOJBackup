import sys
input = sys.stdin.readline

m = int(input())
menu = list(int(input()) for _ in range(m))
s = int(input())
result = 0
for _ in range(s):
    want = int(input())
    result += menu[want-1]
print(result)