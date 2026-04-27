import sys

word = sys.stdin.readline().rstrip()
result = 0
for i in range(len(word)-3):
    if word[i:i+4] == "DKSH":
        result += 1
print(result)