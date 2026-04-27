import sys
input = sys.stdin.readline

n, m = map(int, input().split())
for _ in range(n):
    bung = input().rstrip()
    print(bung[::-1])