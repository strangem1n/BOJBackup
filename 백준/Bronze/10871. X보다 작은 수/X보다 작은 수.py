a, b = map(int, input().split())
n = input()
nlist = n.split()
result = []
for i in range(a):
    if b > int(nlist[i]):
        result.append(nlist[i])
print(" ".join(result))