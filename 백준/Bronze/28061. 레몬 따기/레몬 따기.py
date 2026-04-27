import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))

for i in range(1, n+1):
    tree[-i] -= i

print(max(tree))