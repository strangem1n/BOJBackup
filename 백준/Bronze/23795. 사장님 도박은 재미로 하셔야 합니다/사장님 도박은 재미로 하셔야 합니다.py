import sys
total = 0
while True:
    loss = int(sys.stdin.readline())
    if loss == -1:
        break
    else:
        total += loss
print(total)