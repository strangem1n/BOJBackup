import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    arr = sorted(map(int, input().split()), reverse=True)
    print(arr[2])
