import sys
input = sys.stdin.readline

while True:
    word = input().rstrip()
    if word == '#':
        break
    ans = set()
    for w in word:
        n = ord(w)
        if n > 90:
            n -= 32
        n -= 64
        if 0 < n <= 26:
            ans.add(n)
    print(len(ans))
