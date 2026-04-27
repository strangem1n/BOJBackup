import sys
text = sys.stdin.readline()
textset = set()
for i in range(len(text)):
    for j in range(i, len(text)):
        a = text[i:j]
        textset.add(a)

print(len(textset)-1)