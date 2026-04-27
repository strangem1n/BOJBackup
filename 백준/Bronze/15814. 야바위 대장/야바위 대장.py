import sys
input = sys.stdin.readline


word = list(input().rstrip())
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    word[a], word[b] = word[b], word[a]
print("".join(word))