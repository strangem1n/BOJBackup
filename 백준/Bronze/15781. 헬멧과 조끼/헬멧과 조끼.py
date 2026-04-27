import sys
input = sys.stdin.readline

n, m = map(int, input().split())
helmet = map(int, input().split())
coat = map(int, input().split())
print(max(helmet)+max(coat))