import sys
input = sys.stdin.readline

n = int(input())
word = input().rstrip()
for i in range(0, len(word), n):
    print(word[i], end="")
