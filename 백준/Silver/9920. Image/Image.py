import sys
input = sys.stdin.readline

def divide(n, arr):
    if n == 1:
        return 2
    else:
        half = n // 2
        s = 0
        a = []
        b = []
        c = []
        d = []
        for i in range(n):
            if i < half:
                a.append(arr[i][:half])
                b.append(arr[i][half:])
            else:
                c.append(arr[i][:half])
                d.append(arr[i][half:])
            s += sum(arr[i])
        if s == 0 or s == n ** 2:
            return 2
        else:
            return 1 + divide(half, a) + divide(half, b) + divide(half, c) + divide(half, d)

L = int(input())
array = [list(map(int, input().split())) for _ in range(L)]
print(divide(L, array))