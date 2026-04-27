import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word, i, j = input().split()
    print(word[:int(i)]+word[int(j):])
