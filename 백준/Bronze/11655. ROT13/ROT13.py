import sys

word = sys.stdin.readline().rstrip()
for w in word:
    if 65 <= ord(w) <= 77:
        print(chr(ord(w)+13), end="")
    elif 78 <= ord(w) <= 90:
        print(chr(ord(w)-13), end="")
    elif 97 <= ord(w) <= 109:
        print(chr(ord(w)+13), end="")
    elif 110 <= ord(w) <= 122:
        print(chr(ord(w)-13), end="")
    else:
        print(w, end="")
