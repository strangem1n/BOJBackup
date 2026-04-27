import sys
arr = list(map(int, sys.stdin.readline().split()))
i = min(arr)
while True:
    chk = 0
    for j in range(5):
        if i % arr[j] == 0:
            chk += 1
    if chk >= 3:
        print(i)
        break
    i += 1
