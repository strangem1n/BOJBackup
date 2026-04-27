import sys
input = sys.stdin.readline

n = int(input())
line = [input().split() for _ in range(n)]
for l in line:
    l.reverse()
order = []
for l in line:
    order.extend(l)
order.sort(key=lambda x: (x[0], int(x[2:])), reverse=True)
line.reverse()

wait = []
while line:
    if wait and wait[-1] == order[-1]:
        wait.pop()
        order.pop()
    elif line[-1][-1] == order[-1]:
        line[-1].pop()
        order.pop()
        if not line[-1]:
            line.pop()
    else:
        wait.append(line[-1].pop())
        if not line[-1]:
            line.pop()
while wait:
    if wait[-1] == order[-1]:
        wait.pop()
        order.pop()
    else:
        break
if order:
    print("BAD")
else:
    print("GOOD")