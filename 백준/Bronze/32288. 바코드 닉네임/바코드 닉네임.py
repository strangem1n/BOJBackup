import sys
input = sys.stdin.readline

n = int(input())
code = input().rstrip()
for c in code:
    if c == "I":
        print("i", end="")
    else:
        print("L", end="")
