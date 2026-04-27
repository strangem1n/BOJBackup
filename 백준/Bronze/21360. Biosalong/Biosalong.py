import sys
input = sys.stdin.readline

n = int(input())
chair = list(map(lambda x: len(x), input().rstrip().split(".")))
print(min(chair[1:-1]))
