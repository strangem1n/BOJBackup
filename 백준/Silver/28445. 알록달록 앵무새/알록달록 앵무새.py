import sys
input = sys.stdin.readline

a, b = input().split()
c, d = input().split()
color = sorted({a, b, c, d})
for i in range(len(color)):
    for j in range(len(color)):
        print(color[i], color[j])
