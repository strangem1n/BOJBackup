import sys
input = sys.stdin.readline

n = sorted(map(int, input().split()))
abc = input().rstrip()
for a in abc:
    print(n[ord(a)-65], end=" ")
