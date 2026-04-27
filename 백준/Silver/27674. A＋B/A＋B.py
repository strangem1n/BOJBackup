import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    blank = input()
    arr = list(input().rstrip())
    arr.sort(reverse=True)
    a = int(''.join(arr[:-1]))
    b = int(arr[-1])
    print(a+b)