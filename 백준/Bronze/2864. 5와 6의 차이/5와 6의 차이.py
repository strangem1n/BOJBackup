import sys
input = sys.stdin.readline

a, b = input().split()
an, bn = int(a.replace("6", "5")), int(b.replace("6", "5"))
ax, bx = int(a.replace("5", "6")), int(b.replace("5", "6"))
print(an+bn, ax+bx)
