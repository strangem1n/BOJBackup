import sys
input = sys.stdin.readline

n = int(input())
tab = [int(input()) for _ in range(n)]
print(sum(tab)-n+1)