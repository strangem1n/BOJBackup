import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
for _ in range(n+m):
    if i < n:
        if j == m:
            print(a[i], end=" ")
            i += 1
        elif a[i] <= b[j]:
            print(a[i], end=" ")
            i += 1
        else:
            print(b[j], end=" ")
            j += 1
    else:
        print(b[j], end=" ")
        j += 1
