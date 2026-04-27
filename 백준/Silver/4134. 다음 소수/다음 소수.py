import math
n = int(input())
for _ in range(n):
    a = int(input())
    if a <= 2:
        print(2)
        continue
    else:
        root = int(math.sqrt(a))
        while True:
            check = 0
            for i in range(2, root+2):
                if a % i == 0:
                    check = 1
                    break
            if check == 1:
                a += 1
                continue
            else:
                print(a)
                break