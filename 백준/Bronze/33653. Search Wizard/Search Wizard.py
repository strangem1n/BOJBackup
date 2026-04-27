import sys
input = sys.stdin.readline

word = input().rstrip()
n = int(input())
arr = list(input().split())

result = 0
for a in arr:
    for i in range(len(a)-len(word)+1):
        if a[i:i+len(word)] == word:
            result += 1
print(result)
