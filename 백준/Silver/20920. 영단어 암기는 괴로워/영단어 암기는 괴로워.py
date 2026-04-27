import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    if words.get(word):
        words[word] += 1
    else:
        words[word] = 1
        
data = list(words.items())
data.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for d in data:
    print(d[0])