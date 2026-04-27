import sys
input = sys.stdin.readline
n = int(input())
plan = map(int, input().split())
hour = sum(plan)+ 8*(n-1)
print(hour//24, hour%24)