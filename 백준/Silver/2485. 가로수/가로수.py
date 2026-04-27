import sys, math
n = int(sys.stdin.readline())
tree = []
dif = []

for _ in range(n):
    a = int(sys.stdin.readline())
    tree.append(a)

tree.sort(reverse=True)
for i in range(len(tree)-1):
    m = tree[i] - tree[i+1]
    dif.append(m)

dif = list(set(dif))
gcd_dif = dif[0]
for i in dif[1:]:
    gcd_dif = math.gcd(gcd_dif, i)
    if gcd_dif == 1:
        break

newtree = (max(tree) - min(tree)) / gcd_dif + 1
require = int(newtree) - n
print(require)