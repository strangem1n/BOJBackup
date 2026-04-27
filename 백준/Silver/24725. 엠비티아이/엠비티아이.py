def mbtifind(data, b, a):
    mbti = 0
    for x in range(0, b-3):
        for y in range(a):
            if (
                (data[x][y] == 'E' or data[x][y] == 'I')
                and (data[x+1][y] == 'N' or data[x+1][y] == 'S')
                and (data[x+2][y] == 'F' or data[x+2][y] == 'T')
                and (data[x+3][y] == 'P' or data[x+3][y] == 'J')
                ):
                mbti += 1

    for x in range(3, b):
        for y in range(a):
            if (
                (data[x][y] == 'E' or data[x][y] == 'I')
                and (data[x-1][y] == 'N' or data[x-1][y] == 'S')
                and (data[x-2][y] == 'F' or data[x-2][y] == 'T')
                and (data[x-3][y] == 'P' or data[x-3][y] == 'J')
                ):
                mbti += 1

    for x in range(b):
        for y in range(0, a-3):
            if (
                (data[x][y] == 'E' or data[x][y] == 'I')
                and (data[x][y+1] == 'N' or data[x][y+1] == 'S')
                and (data[x][y+2] == 'F' or data[x][y+2] == 'T')
                and (data[x][y+3] == 'P' or data[x][y+3] == 'J')
                ):
                mbti += 1

    for x in range(b):
        for y in range(3, a):
            if (
                (data[x][y] == 'E' or data[x][y] == 'I')
                and (data[x][y-1] == 'N' or data[x][y-1] == 'S')
                and (data[x][y-2] == 'F' or data[x][y-2] == 'T')
                and (data[x][y-3] == 'P' or data[x][y-3] == 'J')
                ):
                mbti += 1

    for x in range(0, b-3):
        for y in range(0, a-3):
            if (
                (data[x][y] == 'E' or data[x][y] == 'I')
                and (data[x+1][y+1] == 'N' or data[x+1][y+1] == 'S')
                and (data[x+2][y+2] == 'F' or data[x+2][y+2] == 'T')
                and (data[x+3][y+3] == 'P' or data[x+3][y+3] == 'J')
                ):
                mbti += 1

    for x in range(0, b-3):
        for y in range(3, a):
            if (
                (data[x][y] == 'E' or data[x][y] == 'I')
                and (data[x+1][y-1] == 'N' or data[x+1][y-1] == 'S')
                and (data[x+2][y-2] == 'F' or data[x+2][y-2] == 'T')
                and (data[x+3][y-3] == 'P' or data[x+3][y-3] == 'J')
                ):
                mbti += 1

    for x in range(3, b):
        for y in range(0, a-3):
            if (
                (data[x][y] == 'E' or data[x][y] == 'I')
                and (data[x-1][y+1] == 'N' or data[x-1][y+1] == 'S')
                and (data[x-2][y+2] == 'F' or data[x-2][y+2] == 'T')
                and (data[x-3][y+3] == 'P' or data[x-3][y+3] == 'J')
                ):
                mbti += 1

    for x in range(3, b):
        for y in range(3, a):
            if (
                (data[x][y] == 'E' or data[x][y] == 'I')
                and (data[x-1][y-1] == 'N' or data[x-1][y-1] == 'S')
                and (data[x-2][y-2] == 'F' or data[x-2][y-2] == 'T')
                and (data[x-3][y-3] == 'P' or data[x-3][y-3] == 'J')
                ):
                mbti += 1
    return mbti

import sys
n, m = map(int, sys.stdin.readline().split())
data = sys.stdin.read().splitlines()
result = mbtifind(data, n, m)
print(result)
