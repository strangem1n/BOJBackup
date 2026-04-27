import sys

def apart_require(floor, number):
    apart = []

    floor_0 = [x for x in range(1, 15)]
    apart.append(floor_0)
    
    for i in range(1, floor+1):
        new_floor = [0 for _ in range(number)]
        new_floor[0] = 1
        for j in range(1, number):
           new_floor[j] = new_floor[j-1] + apart[i-1][j]
        apart.append(new_floor)

    return apart[floor][number-1]

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    result = apart_require(k, n)
    print(result)