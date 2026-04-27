import sys
input = sys.stdin.readline

r = {"black": 0, "brown": 1, "red":	2, "orange": 3, "yellow": 4,
     "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
ans = 0
ans += r[input().rstrip()] * 10
ans += r[input().rstrip()]
ans *= 10 ** r[input().rstrip()]
print(ans)
