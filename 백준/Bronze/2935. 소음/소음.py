import sys
input = sys.stdin.readline
a = int(input())
p = input().rstrip()
if p == "+":
    a += int(input())
else:
    a *= int(input())
print(a)
