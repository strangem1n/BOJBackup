import sys
n = int(sys.stdin.readline())
idx_1 = {}
for _ in range(n):
    i = int(sys.stdin.readline())
    if i in idx_1:
        idx_1[i] += 1
    else:
        idx_1[i] = 1

keys = idx_1.keys()

idx_2 = list(keys)
idx_2.sort()

for idx in idx_2:
    count = idx_1.get(idx)
    for _ in range(count):
        print(idx)