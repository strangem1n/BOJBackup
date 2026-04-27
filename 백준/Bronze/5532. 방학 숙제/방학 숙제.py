import sys
input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

lang = a // c
if a % c > 0:
    lang += 1
math = b // d
if b % d > 0:
    math += 1
print(l - max(lang, math))